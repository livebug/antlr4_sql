from antlr4 import CommonTokenStream, ParseTreeWalker
from antlr4.InputStream import InputStream
from tdh.antlr4.HiveLexer import HiveLexer as SqlLexer
from tdh.antlr4.HiveParser import HiveParser as SqlParser
from tdh.antlr4.HiveParserListener import HiveParserListener as SqlListener
from collections import deque
import pydot

from tdh_antlr4_test import print_tree_like_linux, save_dot_file


# 解析SQL脚本，获取表名和关联表
def parse_sql(sql_script):
    input_stream = InputStream(sql_script)
    lexer = SqlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SqlParser(stream)
    tree = parser.statement()

    save_dot_file(tree, parser, "output.dot")

    return tree


# 自定义监听器，提取表名和关联表
class TableListener(SqlListener):
    def __init__(self):
        self.tables = set()
        self.relations = []
        self.stack = deque()
        self.subQueryStack = deque()
        self.insert = (False, None)

    def enterInsertClause(self, ctx):
        table_name = ctx.tableOrPartition().tableName().getText().lower()
        self.tables.add(table_name)
        self.stack.append(table_name)

    def exitRegularBody(self, ctx):
        if self.stack.__len__() > 0:
            self.stack.pop()
        return super().exitRegularBody(ctx)

    def enterAtomjoinSource(self, ctx):
        if ctx.tableSource():
            table_name = ctx.tableSource().getText().lower()
            self.tables.add(table_name)
            if len(self.subQueryStack) > 0:
                right_table = self.subQueryStack[-1]
                self.relations.append((table_name, right_table, {"label": "insert"}))

        if ctx.subQuerySource():
            table_name = "subquery#" + ctx.subQuerySource().getText().lower()
            self.tables.add(table_name)
            if len(self.stack) > 0:
                self.relations.append((table_name, self.stack[-1], {"label": "insert"}))
            self.subQueryStack.append(table_name)

    def exitSubQuerySource(self, ctx):
        if not isinstance(ctx.parentCtx, SqlParser.AtomjoinSourceContext):
            if self.subQueryStack.__len__() > 0:
                self.subQueryStack.pop()
        return super().exitSubQuerySource(ctx)

    def existJoinSource(self, ctx):
        if self.subQueryStack.__len__() > 0:
            self.subQueryStack.pop()
        return super().existJoinSource(ctx)

    def enterOtherjoinSource(self, ctx):
        if len(self.subQueryStack) > 0:
            right_table = self.subQueryStack[-1]
        else:
            right_table = ctx.parentCtx.atomjoinSource().getText()
        if ctx.joinSourcePart().tableSource():
            left_table = ctx.joinSourcePart().getText().lower()
            label = ctx.joinToken().getText().lower()
            self.relations.append(
                (
                    left_table,
                    right_table,
                    {"label": label, "style": "dashed", "dir": "none"},
                )
            )

        if ctx.joinSourcePart().subQuerySource():
            left_table = "subquery#" + ctx.joinSourcePart().getText().lower()
            label = ctx.joinToken().getText().lower()
            self.subQueryStack.append(left_table)
            self.relations.append(
                (
                    left_table,
                    right_table,
                    {"label": label, "style": "dashed", "dir": "none"},
                )
            )


# 获取表名和关联表
def get_tables_and_relations(tree):
    listener = TableListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.tables, listener.relations


# 绘制表级数据流项图（dot）
def draw_data_flow_graph(tables, relations, output_file):
    graph = pydot.Dot(graph_type="digraph")
    for table in tables:
        node = pydot.Node(table)
        graph.add_node(node)
    for left_table, right_table, config in relations:
        label = config.get("label", "")
        style = config.get("style", "solid")
        direction = config.get("dir", "forward")
        edge = pydot.Edge(
            left_table,
            right_table,
            label=label,
            style=style,
            dir=direction,
        )
        graph.add_edge(edge)
    graph.write(output_file)


# 主函数，处理SQL脚本并绘制数据流图
def main(sql_script, output_file):
    tree = parse_sql(sql_script)
    tables, relations = get_tables_and_relations(tree)
    draw_data_flow_graph(tables, relations, output_file)


if __name__ == "__main__":
    sql_script = """
    insert into table4
    SELECT * FROM (select id from users where age > 20 ) AS table1
    JOIN (select * from table2 ) t2 ON table1.id = t2.id
    LEFT JOIN table3 ON table3.id = t2.cid
    """
    output_file = "data_flow_graph.dot"
    main(sql_script, output_file)
