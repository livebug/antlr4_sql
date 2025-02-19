from antlr4 import CommonTokenStream, ParseTreeWalker
from antlr4.InputStream import InputStream
from tdh.antlr4.HiveLexer import HiveLexer as SqlLexer
from tdh.antlr4.HiveParser import HiveParser as SqlParser
from tdh.antlr4.HiveParserListener import HiveParserListener as SqlListener
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
        self.insert = (False, None)
    
    def enterInsertClause(self, ctx):
        table_name = ctx.tableOrPartition().tableName().getText()
        self.tables.add(table_name)
        self.insert = (True, table_name)

    def enterAtomjoinSource(self, ctx):
        table_name = ctx.getText()
        self.tables.add(table_name)
        if self.insert[0]:
            self.relations.append((table_name, self.insert[1], 'insert'))
            self.insert = (False, None)

    def enterOtherjoinSource(self, ctx):
        right_table = ctx.parentCtx.atomjoinSource().getText()
        left_table = ctx.joinSourcePart().getText()
        label = ctx.joinToken().getText()
        self.relations.append((left_table, right_table,label))

# 获取表名和关联表
def get_tables_and_relations(tree):
    listener = TableListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.tables, listener.relations

# 绘制表级数据流项图（dot）
def draw_data_flow_graph(tables, relations, output_file):
    graph = pydot.Dot(graph_type='digraph')
    for table in tables:
        node = pydot.Node(table)
        graph.add_node(node)
    for left_table, right_table,label in relations:
        edge = pydot.Edge(left_table, right_table, label=label)
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
    SELECT * FROM table1
    JOIN table2 ON table1.id = table2.id
    LEFT JOIN table3 ON table3.id = table2.cid
    """
    output_file = "data_flow_graph.dot"
    main(sql_script, output_file)