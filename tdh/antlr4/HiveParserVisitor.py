# Generated from F:/2025/antlr4_sql/tdh/grammar/HiveParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HiveParser import HiveParser
else:
    from HiveParser import HiveParser

# This class defines a complete generic visitor for a parse tree produced by HiveParser.

class HiveParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HiveParser#statement.
    def visitStatement(self, ctx:HiveParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#explainStatement.
    def visitExplainStatement(self, ctx:HiveParser.ExplainStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#explainOption.
    def visitExplainOption(self, ctx:HiveParser.ExplainOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#vectorizationOnly.
    def visitVectorizationOnly(self, ctx:HiveParser.VectorizationOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#vectorizatonDetail.
    def visitVectorizatonDetail(self, ctx:HiveParser.VectorizatonDetailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#execStatement.
    def visitExecStatement(self, ctx:HiveParser.ExecStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#loadStatement.
    def visitLoadStatement(self, ctx:HiveParser.LoadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#replicationClause.
    def visitReplicationClause(self, ctx:HiveParser.ReplicationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#exportStatement.
    def visitExportStatement(self, ctx:HiveParser.ExportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#importStatement.
    def visitImportStatement(self, ctx:HiveParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#replDumpStatement.
    def visitReplDumpStatement(self, ctx:HiveParser.ReplDumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#replDbPolicy.
    def visitReplDbPolicy(self, ctx:HiveParser.ReplDbPolicyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#replLoadStatement.
    def visitReplLoadStatement(self, ctx:HiveParser.ReplLoadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#replConfigs.
    def visitReplConfigs(self, ctx:HiveParser.ReplConfigsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#replConfigsList.
    def visitReplConfigsList(self, ctx:HiveParser.ReplConfigsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#replTableLevelPolicy.
    def visitReplTableLevelPolicy(self, ctx:HiveParser.ReplTableLevelPolicyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#replStatusStatement.
    def visitReplStatusStatement(self, ctx:HiveParser.ReplStatusStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#ddlStatement.
    def visitDdlStatement(self, ctx:HiveParser.DdlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#ifExists.
    def visitIfExists(self, ctx:HiveParser.IfExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#restrictOrCascade.
    def visitRestrictOrCascade(self, ctx:HiveParser.RestrictOrCascadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#ifNotExists.
    def visitIfNotExists(self, ctx:HiveParser.IfNotExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#force.
    def visitForce(self, ctx:HiveParser.ForceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#rewriteEnabled.
    def visitRewriteEnabled(self, ctx:HiveParser.RewriteEnabledContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#rewriteDisabled.
    def visitRewriteDisabled(self, ctx:HiveParser.RewriteDisabledContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#storedAsDirs.
    def visitStoredAsDirs(self, ctx:HiveParser.StoredAsDirsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#orReplace.
    def visitOrReplace(self, ctx:HiveParser.OrReplaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createDatabaseStatement.
    def visitCreateDatabaseStatement(self, ctx:HiveParser.CreateDatabaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dbLocation.
    def visitDbLocation(self, ctx:HiveParser.DbLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dbManagedLocation.
    def visitDbManagedLocation(self, ctx:HiveParser.DbManagedLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dbProperties.
    def visitDbProperties(self, ctx:HiveParser.DbPropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dbPropertiesList.
    def visitDbPropertiesList(self, ctx:HiveParser.DbPropertiesListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dbConnectorName.
    def visitDbConnectorName(self, ctx:HiveParser.DbConnectorNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#switchDatabaseStatement.
    def visitSwitchDatabaseStatement(self, ctx:HiveParser.SwitchDatabaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropDatabaseStatement.
    def visitDropDatabaseStatement(self, ctx:HiveParser.DropDatabaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#databaseComment.
    def visitDatabaseComment(self, ctx:HiveParser.DatabaseCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#truncateTableStatement.
    def visitTruncateTableStatement(self, ctx:HiveParser.TruncateTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropTableStatement.
    def visitDropTableStatement(self, ctx:HiveParser.DropTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#inputFileFormat.
    def visitInputFileFormat(self, ctx:HiveParser.InputFileFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tabTypeExpr.
    def visitTabTypeExpr(self, ctx:HiveParser.TabTypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partTypeExpr.
    def visitPartTypeExpr(self, ctx:HiveParser.PartTypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tabPartColTypeExpr.
    def visitTabPartColTypeExpr(self, ctx:HiveParser.TabPartColTypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#descStatement.
    def visitDescStatement(self, ctx:HiveParser.DescStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#analyzeStatement.
    def visitAnalyzeStatement(self, ctx:HiveParser.AnalyzeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#from_in.
    def visitFrom_in(self, ctx:HiveParser.From_inContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#db_schema.
    def visitDb_schema(self, ctx:HiveParser.Db_schemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#showStatement.
    def visitShowStatement(self, ctx:HiveParser.ShowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#showTablesFilterExpr.
    def visitShowTablesFilterExpr(self, ctx:HiveParser.ShowTablesFilterExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#lockStatement.
    def visitLockStatement(self, ctx:HiveParser.LockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#lockDatabase.
    def visitLockDatabase(self, ctx:HiveParser.LockDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#lockMode.
    def visitLockMode(self, ctx:HiveParser.LockModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#unlockStatement.
    def visitUnlockStatement(self, ctx:HiveParser.UnlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#unlockDatabase.
    def visitUnlockDatabase(self, ctx:HiveParser.UnlockDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createRoleStatement.
    def visitCreateRoleStatement(self, ctx:HiveParser.CreateRoleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropRoleStatement.
    def visitDropRoleStatement(self, ctx:HiveParser.DropRoleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#grantPrivileges.
    def visitGrantPrivileges(self, ctx:HiveParser.GrantPrivilegesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#revokePrivileges.
    def visitRevokePrivileges(self, ctx:HiveParser.RevokePrivilegesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#grantRole.
    def visitGrantRole(self, ctx:HiveParser.GrantRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#revokeRole.
    def visitRevokeRole(self, ctx:HiveParser.RevokeRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#showRoleGrants.
    def visitShowRoleGrants(self, ctx:HiveParser.ShowRoleGrantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#showRoles.
    def visitShowRoles(self, ctx:HiveParser.ShowRolesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#showCurrentRole.
    def visitShowCurrentRole(self, ctx:HiveParser.ShowCurrentRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#setRole.
    def visitSetRole(self, ctx:HiveParser.SetRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#showGrants.
    def visitShowGrants(self, ctx:HiveParser.ShowGrantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#showRolePrincipals.
    def visitShowRolePrincipals(self, ctx:HiveParser.ShowRolePrincipalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#privilegeIncludeColObject.
    def visitPrivilegeIncludeColObject(self, ctx:HiveParser.PrivilegeIncludeColObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#privilegeObject.
    def visitPrivilegeObject(self, ctx:HiveParser.PrivilegeObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#privObject.
    def visitPrivObject(self, ctx:HiveParser.PrivObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#privObjectCols.
    def visitPrivObjectCols(self, ctx:HiveParser.PrivObjectColsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#privilegeList.
    def visitPrivilegeList(self, ctx:HiveParser.PrivilegeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#privlegeDef.
    def visitPrivlegeDef(self, ctx:HiveParser.PrivlegeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#privilegeType.
    def visitPrivilegeType(self, ctx:HiveParser.PrivilegeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#principalSpecification.
    def visitPrincipalSpecification(self, ctx:HiveParser.PrincipalSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#principalName.
    def visitPrincipalName(self, ctx:HiveParser.PrincipalNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#withGrantOption.
    def visitWithGrantOption(self, ctx:HiveParser.WithGrantOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#grantOptionFor.
    def visitGrantOptionFor(self, ctx:HiveParser.GrantOptionForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#adminOptionFor.
    def visitAdminOptionFor(self, ctx:HiveParser.AdminOptionForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#withAdminOption.
    def visitWithAdminOption(self, ctx:HiveParser.WithAdminOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#metastoreCheck.
    def visitMetastoreCheck(self, ctx:HiveParser.MetastoreCheckContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#resourceList.
    def visitResourceList(self, ctx:HiveParser.ResourceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#resource.
    def visitResource(self, ctx:HiveParser.ResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#resourceType.
    def visitResourceType(self, ctx:HiveParser.ResourceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createFunctionStatement.
    def visitCreateFunctionStatement(self, ctx:HiveParser.CreateFunctionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropFunctionStatement.
    def visitDropFunctionStatement(self, ctx:HiveParser.DropFunctionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#reloadFunctionsStatement.
    def visitReloadFunctionsStatement(self, ctx:HiveParser.ReloadFunctionsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createMacroStatement.
    def visitCreateMacroStatement(self, ctx:HiveParser.CreateMacroStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropMacroStatement.
    def visitDropMacroStatement(self, ctx:HiveParser.DropMacroStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createViewStatement.
    def visitCreateViewStatement(self, ctx:HiveParser.CreateViewStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#viewPartition.
    def visitViewPartition(self, ctx:HiveParser.ViewPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#viewOrganization.
    def visitViewOrganization(self, ctx:HiveParser.ViewOrganizationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#viewClusterSpec.
    def visitViewClusterSpec(self, ctx:HiveParser.ViewClusterSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#viewComplexSpec.
    def visitViewComplexSpec(self, ctx:HiveParser.ViewComplexSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#viewDistSpec.
    def visitViewDistSpec(self, ctx:HiveParser.ViewDistSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#viewSortSpec.
    def visitViewSortSpec(self, ctx:HiveParser.ViewSortSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropViewStatement.
    def visitDropViewStatement(self, ctx:HiveParser.DropViewStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createMaterializedViewStatement.
    def visitCreateMaterializedViewStatement(self, ctx:HiveParser.CreateMaterializedViewStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropMaterializedViewStatement.
    def visitDropMaterializedViewStatement(self, ctx:HiveParser.DropMaterializedViewStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createScheduledQueryStatement.
    def visitCreateScheduledQueryStatement(self, ctx:HiveParser.CreateScheduledQueryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropScheduledQueryStatement.
    def visitDropScheduledQueryStatement(self, ctx:HiveParser.DropScheduledQueryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterScheduledQueryStatement.
    def visitAlterScheduledQueryStatement(self, ctx:HiveParser.AlterScheduledQueryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterScheduledQueryChange.
    def visitAlterScheduledQueryChange(self, ctx:HiveParser.AlterScheduledQueryChangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#scheduleSpec.
    def visitScheduleSpec(self, ctx:HiveParser.ScheduleSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#executedAsSpec.
    def visitExecutedAsSpec(self, ctx:HiveParser.ExecutedAsSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#definedAsSpec.
    def visitDefinedAsSpec(self, ctx:HiveParser.DefinedAsSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#showFunctionIdentifier.
    def visitShowFunctionIdentifier(self, ctx:HiveParser.ShowFunctionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#showStmtIdentifier.
    def visitShowStmtIdentifier(self, ctx:HiveParser.ShowStmtIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableComment.
    def visitTableComment(self, ctx:HiveParser.TableCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createTablePartitionSpec.
    def visitCreateTablePartitionSpec(self, ctx:HiveParser.CreateTablePartitionSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createTablePartitionColumnTypeSpec.
    def visitCreateTablePartitionColumnTypeSpec(self, ctx:HiveParser.CreateTablePartitionColumnTypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createTablePartitionColumnSpec.
    def visitCreateTablePartitionColumnSpec(self, ctx:HiveParser.CreateTablePartitionColumnSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partitionTransformSpec.
    def visitPartitionTransformSpec(self, ctx:HiveParser.PartitionTransformSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameTransformConstraint.
    def visitColumnNameTransformConstraint(self, ctx:HiveParser.ColumnNameTransformConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partitionTransformType.
    def visitPartitionTransformType(self, ctx:HiveParser.PartitionTransformTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableBuckets.
    def visitTableBuckets(self, ctx:HiveParser.TableBucketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableImplBuckets.
    def visitTableImplBuckets(self, ctx:HiveParser.TableImplBucketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableSkewed.
    def visitTableSkewed(self, ctx:HiveParser.TableSkewedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#rowFormat.
    def visitRowFormat(self, ctx:HiveParser.RowFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#recordReader.
    def visitRecordReader(self, ctx:HiveParser.RecordReaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#recordWriter.
    def visitRecordWriter(self, ctx:HiveParser.RecordWriterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#rowFormatSerde.
    def visitRowFormatSerde(self, ctx:HiveParser.RowFormatSerdeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#rowFormatDelimited.
    def visitRowFormatDelimited(self, ctx:HiveParser.RowFormatDelimitedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableRowFormat.
    def visitTableRowFormat(self, ctx:HiveParser.TableRowFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tablePropertiesPrefixed.
    def visitTablePropertiesPrefixed(self, ctx:HiveParser.TablePropertiesPrefixedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableProperties.
    def visitTableProperties(self, ctx:HiveParser.TablePropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tablePropertiesList.
    def visitTablePropertiesList(self, ctx:HiveParser.TablePropertiesListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#keyValueProperty.
    def visitKeyValueProperty(self, ctx:HiveParser.KeyValuePropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#keyProperty.
    def visitKeyProperty(self, ctx:HiveParser.KeyPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableRowFormatFieldIdentifier.
    def visitTableRowFormatFieldIdentifier(self, ctx:HiveParser.TableRowFormatFieldIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableRowFormatCollItemsIdentifier.
    def visitTableRowFormatCollItemsIdentifier(self, ctx:HiveParser.TableRowFormatCollItemsIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableRowFormatMapKeysIdentifier.
    def visitTableRowFormatMapKeysIdentifier(self, ctx:HiveParser.TableRowFormatMapKeysIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableRowFormatLinesIdentifier.
    def visitTableRowFormatLinesIdentifier(self, ctx:HiveParser.TableRowFormatLinesIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableRowNullFormat.
    def visitTableRowNullFormat(self, ctx:HiveParser.TableRowNullFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableFileFormat.
    def visitTableFileFormat(self, ctx:HiveParser.TableFileFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableLocation.
    def visitTableLocation(self, ctx:HiveParser.TableLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameTypeList.
    def visitColumnNameTypeList(self, ctx:HiveParser.ColumnNameTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameTypeOrConstraintList.
    def visitColumnNameTypeOrConstraintList(self, ctx:HiveParser.ColumnNameTypeOrConstraintListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameColonTypeList.
    def visitColumnNameColonTypeList(self, ctx:HiveParser.ColumnNameColonTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameList.
    def visitColumnNameList(self, ctx:HiveParser.ColumnNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnName.
    def visitColumnName(self, ctx:HiveParser.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#extColumnName.
    def visitExtColumnName(self, ctx:HiveParser.ExtColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameOrderList.
    def visitColumnNameOrderList(self, ctx:HiveParser.ColumnNameOrderListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnParenthesesList.
    def visitColumnParenthesesList(self, ctx:HiveParser.ColumnParenthesesListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#enableValidateSpecification.
    def visitEnableValidateSpecification(self, ctx:HiveParser.EnableValidateSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#enableSpecification.
    def visitEnableSpecification(self, ctx:HiveParser.EnableSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#validateSpecification.
    def visitValidateSpecification(self, ctx:HiveParser.ValidateSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#enforcedSpecification.
    def visitEnforcedSpecification(self, ctx:HiveParser.EnforcedSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#relySpecification.
    def visitRelySpecification(self, ctx:HiveParser.RelySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createConstraint.
    def visitCreateConstraint(self, ctx:HiveParser.CreateConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterConstraintWithName.
    def visitAlterConstraintWithName(self, ctx:HiveParser.AlterConstraintWithNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableLevelConstraint.
    def visitTableLevelConstraint(self, ctx:HiveParser.TableLevelConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#pkUkConstraint.
    def visitPkUkConstraint(self, ctx:HiveParser.PkUkConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#checkConstraint.
    def visitCheckConstraint(self, ctx:HiveParser.CheckConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createForeignKey.
    def visitCreateForeignKey(self, ctx:HiveParser.CreateForeignKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterForeignKeyWithName.
    def visitAlterForeignKeyWithName(self, ctx:HiveParser.AlterForeignKeyWithNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#skewedValueElement.
    def visitSkewedValueElement(self, ctx:HiveParser.SkewedValueElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#skewedColumnValuePairList.
    def visitSkewedColumnValuePairList(self, ctx:HiveParser.SkewedColumnValuePairListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#skewedColumnValuePair.
    def visitSkewedColumnValuePair(self, ctx:HiveParser.SkewedColumnValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#skewedColumnValues.
    def visitSkewedColumnValues(self, ctx:HiveParser.SkewedColumnValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#skewedColumnValue.
    def visitSkewedColumnValue(self, ctx:HiveParser.SkewedColumnValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#skewedValueLocationElement.
    def visitSkewedValueLocationElement(self, ctx:HiveParser.SkewedValueLocationElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#orderSpecification.
    def visitOrderSpecification(self, ctx:HiveParser.OrderSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#nullOrdering.
    def visitNullOrdering(self, ctx:HiveParser.NullOrderingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameOrder.
    def visitColumnNameOrder(self, ctx:HiveParser.ColumnNameOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameCommentList.
    def visitColumnNameCommentList(self, ctx:HiveParser.ColumnNameCommentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameComment.
    def visitColumnNameComment(self, ctx:HiveParser.ColumnNameCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#orderSpecificationRewrite.
    def visitOrderSpecificationRewrite(self, ctx:HiveParser.OrderSpecificationRewriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnRefOrder.
    def visitColumnRefOrder(self, ctx:HiveParser.ColumnRefOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameType.
    def visitColumnNameType(self, ctx:HiveParser.ColumnNameTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameTypeOrConstraint.
    def visitColumnNameTypeOrConstraint(self, ctx:HiveParser.ColumnNameTypeOrConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableConstraint.
    def visitTableConstraint(self, ctx:HiveParser.TableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameTypeConstraint.
    def visitColumnNameTypeConstraint(self, ctx:HiveParser.ColumnNameTypeConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnConstraint.
    def visitColumnConstraint(self, ctx:HiveParser.ColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#foreignKeyConstraint.
    def visitForeignKeyConstraint(self, ctx:HiveParser.ForeignKeyConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#colConstraint.
    def visitColConstraint(self, ctx:HiveParser.ColConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterColumnConstraint.
    def visitAlterColumnConstraint(self, ctx:HiveParser.AlterColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterForeignKeyConstraint.
    def visitAlterForeignKeyConstraint(self, ctx:HiveParser.AlterForeignKeyConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterColConstraint.
    def visitAlterColConstraint(self, ctx:HiveParser.AlterColConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnConstraintType.
    def visitColumnConstraintType(self, ctx:HiveParser.ColumnConstraintTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#defaultVal.
    def visitDefaultVal(self, ctx:HiveParser.DefaultValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableConstraintType.
    def visitTableConstraintType(self, ctx:HiveParser.TableConstraintTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#constraintOptsCreate.
    def visitConstraintOptsCreate(self, ctx:HiveParser.ConstraintOptsCreateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#constraintOptsAlter.
    def visitConstraintOptsAlter(self, ctx:HiveParser.ConstraintOptsAlterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnNameColonType.
    def visitColumnNameColonType(self, ctx:HiveParser.ColumnNameColonTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#colType.
    def visitColType(self, ctx:HiveParser.ColTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#colTypeList.
    def visitColTypeList(self, ctx:HiveParser.ColTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#type.
    def visitType(self, ctx:HiveParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#primitiveType.
    def visitPrimitiveType(self, ctx:HiveParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#listType.
    def visitListType(self, ctx:HiveParser.ListTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#structType.
    def visitStructType(self, ctx:HiveParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#mapType.
    def visitMapType(self, ctx:HiveParser.MapTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#unionType.
    def visitUnionType(self, ctx:HiveParser.UnionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#setOperator.
    def visitSetOperator(self, ctx:HiveParser.SetOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#queryStatementExpression.
    def visitQueryStatementExpression(self, ctx:HiveParser.QueryStatementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#queryStatementExpressionBody.
    def visitQueryStatementExpressionBody(self, ctx:HiveParser.QueryStatementExpressionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#withClause.
    def visitWithClause(self, ctx:HiveParser.WithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#cteStatement.
    def visitCteStatement(self, ctx:HiveParser.CteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#fromStatement.
    def visitFromStatement(self, ctx:HiveParser.FromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#singleFromStatement.
    def visitSingleFromStatement(self, ctx:HiveParser.SingleFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#regularBody.
    def visitRegularBody(self, ctx:HiveParser.RegularBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#atomSelectStatement.
    def visitAtomSelectStatement(self, ctx:HiveParser.AtomSelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#selectStatement.
    def visitSelectStatement(self, ctx:HiveParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#setOpSelectStatement.
    def visitSetOpSelectStatement(self, ctx:HiveParser.SetOpSelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#selectStatementWithCTE.
    def visitSelectStatementWithCTE(self, ctx:HiveParser.SelectStatementWithCTEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#body.
    def visitBody(self, ctx:HiveParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#insertClause.
    def visitInsertClause(self, ctx:HiveParser.InsertClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#destination.
    def visitDestination(self, ctx:HiveParser.DestinationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#limitClause.
    def visitLimitClause(self, ctx:HiveParser.LimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#deleteStatement.
    def visitDeleteStatement(self, ctx:HiveParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnAssignmentClause.
    def visitColumnAssignmentClause(self, ctx:HiveParser.ColumnAssignmentClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedencePlusExpressionOrDefault.
    def visitPrecedencePlusExpressionOrDefault(self, ctx:HiveParser.PrecedencePlusExpressionOrDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#setColumnsClause.
    def visitSetColumnsClause(self, ctx:HiveParser.SetColumnsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#updateStatement.
    def visitUpdateStatement(self, ctx:HiveParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#sqlTransactionStatement.
    def visitSqlTransactionStatement(self, ctx:HiveParser.SqlTransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#startTransactionStatement.
    def visitStartTransactionStatement(self, ctx:HiveParser.StartTransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#transactionMode.
    def visitTransactionMode(self, ctx:HiveParser.TransactionModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#transactionAccessMode.
    def visitTransactionAccessMode(self, ctx:HiveParser.TransactionAccessModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#isolationLevel.
    def visitIsolationLevel(self, ctx:HiveParser.IsolationLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#levelOfIsolation.
    def visitLevelOfIsolation(self, ctx:HiveParser.LevelOfIsolationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#commitStatement.
    def visitCommitStatement(self, ctx:HiveParser.CommitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#rollbackStatement.
    def visitRollbackStatement(self, ctx:HiveParser.RollbackStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#setAutoCommitStatement.
    def visitSetAutoCommitStatement(self, ctx:HiveParser.SetAutoCommitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#abortTransactionStatement.
    def visitAbortTransactionStatement(self, ctx:HiveParser.AbortTransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#abortCompactionStatement.
    def visitAbortCompactionStatement(self, ctx:HiveParser.AbortCompactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#mergeStatement.
    def visitMergeStatement(self, ctx:HiveParser.MergeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#whenClauses.
    def visitWhenClauses(self, ctx:HiveParser.WhenClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#whenNotMatchedClause.
    def visitWhenNotMatchedClause(self, ctx:HiveParser.WhenNotMatchedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#whenMatchedAndClause.
    def visitWhenMatchedAndClause(self, ctx:HiveParser.WhenMatchedAndClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#whenMatchedThenClause.
    def visitWhenMatchedThenClause(self, ctx:HiveParser.WhenMatchedThenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#updateOrDelete.
    def visitUpdateOrDelete(self, ctx:HiveParser.UpdateOrDeleteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#killQueryStatement.
    def visitKillQueryStatement(self, ctx:HiveParser.KillQueryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#compactionId.
    def visitCompactionId(self, ctx:HiveParser.CompactionIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#compactionPool.
    def visitCompactionPool(self, ctx:HiveParser.CompactionPoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#compactionType.
    def visitCompactionType(self, ctx:HiveParser.CompactionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#compactionStatus.
    def visitCompactionStatus(self, ctx:HiveParser.CompactionStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatement.
    def visitAlterStatement(self, ctx:HiveParser.AlterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterTableStatementSuffix.
    def visitAlterTableStatementSuffix(self, ctx:HiveParser.AlterTableStatementSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterTblPartitionStatementSuffix.
    def visitAlterTblPartitionStatementSuffix(self, ctx:HiveParser.AlterTblPartitionStatementSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementPartitionKeyType.
    def visitAlterStatementPartitionKeyType(self, ctx:HiveParser.AlterStatementPartitionKeyTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterViewStatementSuffix.
    def visitAlterViewStatementSuffix(self, ctx:HiveParser.AlterViewStatementSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterMaterializedViewStatementSuffix.
    def visitAlterMaterializedViewStatementSuffix(self, ctx:HiveParser.AlterMaterializedViewStatementSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterMaterializedViewSuffixRewrite.
    def visitAlterMaterializedViewSuffixRewrite(self, ctx:HiveParser.AlterMaterializedViewSuffixRewriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterMaterializedViewSuffixRebuild.
    def visitAlterMaterializedViewSuffixRebuild(self, ctx:HiveParser.AlterMaterializedViewSuffixRebuildContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterDatabaseStatementSuffix.
    def visitAlterDatabaseStatementSuffix(self, ctx:HiveParser.AlterDatabaseStatementSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterDatabaseSuffixProperties.
    def visitAlterDatabaseSuffixProperties(self, ctx:HiveParser.AlterDatabaseSuffixPropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterDatabaseSuffixSetOwner.
    def visitAlterDatabaseSuffixSetOwner(self, ctx:HiveParser.AlterDatabaseSuffixSetOwnerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterDatabaseSuffixSetLocation.
    def visitAlterDatabaseSuffixSetLocation(self, ctx:HiveParser.AlterDatabaseSuffixSetLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterDatabaseSuffixSetManagedLocation.
    def visitAlterDatabaseSuffixSetManagedLocation(self, ctx:HiveParser.AlterDatabaseSuffixSetManagedLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixRename.
    def visitAlterStatementSuffixRename(self, ctx:HiveParser.AlterStatementSuffixRenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixAddCol.
    def visitAlterStatementSuffixAddCol(self, ctx:HiveParser.AlterStatementSuffixAddColContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixAddConstraint.
    def visitAlterStatementSuffixAddConstraint(self, ctx:HiveParser.AlterStatementSuffixAddConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixUpdateColumns.
    def visitAlterStatementSuffixUpdateColumns(self, ctx:HiveParser.AlterStatementSuffixUpdateColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixDropConstraint.
    def visitAlterStatementSuffixDropConstraint(self, ctx:HiveParser.AlterStatementSuffixDropConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixRenameCol.
    def visitAlterStatementSuffixRenameCol(self, ctx:HiveParser.AlterStatementSuffixRenameColContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixUpdateStatsCol.
    def visitAlterStatementSuffixUpdateStatsCol(self, ctx:HiveParser.AlterStatementSuffixUpdateStatsColContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixUpdateStats.
    def visitAlterStatementSuffixUpdateStats(self, ctx:HiveParser.AlterStatementSuffixUpdateStatsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementChangeColPosition.
    def visitAlterStatementChangeColPosition(self, ctx:HiveParser.AlterStatementChangeColPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixAddPartitions.
    def visitAlterStatementSuffixAddPartitions(self, ctx:HiveParser.AlterStatementSuffixAddPartitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixAddPartitionsElement.
    def visitAlterStatementSuffixAddPartitionsElement(self, ctx:HiveParser.AlterStatementSuffixAddPartitionsElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixTouch.
    def visitAlterStatementSuffixTouch(self, ctx:HiveParser.AlterStatementSuffixTouchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixArchive.
    def visitAlterStatementSuffixArchive(self, ctx:HiveParser.AlterStatementSuffixArchiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixUnArchive.
    def visitAlterStatementSuffixUnArchive(self, ctx:HiveParser.AlterStatementSuffixUnArchiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partitionLocation.
    def visitPartitionLocation(self, ctx:HiveParser.PartitionLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixDropPartitions.
    def visitAlterStatementSuffixDropPartitions(self, ctx:HiveParser.AlterStatementSuffixDropPartitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixProperties.
    def visitAlterStatementSuffixProperties(self, ctx:HiveParser.AlterStatementSuffixPropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterViewSuffixProperties.
    def visitAlterViewSuffixProperties(self, ctx:HiveParser.AlterViewSuffixPropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixSerdeProperties.
    def visitAlterStatementSuffixSerdeProperties(self, ctx:HiveParser.AlterStatementSuffixSerdePropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tablePartitionPrefix.
    def visitTablePartitionPrefix(self, ctx:HiveParser.TablePartitionPrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixFileFormat.
    def visitAlterStatementSuffixFileFormat(self, ctx:HiveParser.AlterStatementSuffixFileFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixClusterbySortby.
    def visitAlterStatementSuffixClusterbySortby(self, ctx:HiveParser.AlterStatementSuffixClusterbySortbyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterTblPartitionStatementSuffixSkewedLocation.
    def visitAlterTblPartitionStatementSuffixSkewedLocation(self, ctx:HiveParser.AlterTblPartitionStatementSuffixSkewedLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#skewedLocations.
    def visitSkewedLocations(self, ctx:HiveParser.SkewedLocationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#skewedLocationsList.
    def visitSkewedLocationsList(self, ctx:HiveParser.SkewedLocationsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#skewedLocationMap.
    def visitSkewedLocationMap(self, ctx:HiveParser.SkewedLocationMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixLocation.
    def visitAlterStatementSuffixLocation(self, ctx:HiveParser.AlterStatementSuffixLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixSkewedby.
    def visitAlterStatementSuffixSkewedby(self, ctx:HiveParser.AlterStatementSuffixSkewedbyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixExchangePartition.
    def visitAlterStatementSuffixExchangePartition(self, ctx:HiveParser.AlterStatementSuffixExchangePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixRenamePart.
    def visitAlterStatementSuffixRenamePart(self, ctx:HiveParser.AlterStatementSuffixRenamePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixStatsPart.
    def visitAlterStatementSuffixStatsPart(self, ctx:HiveParser.AlterStatementSuffixStatsPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixMergeFiles.
    def visitAlterStatementSuffixMergeFiles(self, ctx:HiveParser.AlterStatementSuffixMergeFilesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixBucketNum.
    def visitAlterStatementSuffixBucketNum(self, ctx:HiveParser.AlterStatementSuffixBucketNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#blocking.
    def visitBlocking(self, ctx:HiveParser.BlockingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#compactPool.
    def visitCompactPool(self, ctx:HiveParser.CompactPoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixCompact.
    def visitAlterStatementSuffixCompact(self, ctx:HiveParser.AlterStatementSuffixCompactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixSetOwner.
    def visitAlterStatementSuffixSetOwner(self, ctx:HiveParser.AlterStatementSuffixSetOwnerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixSetPartSpec.
    def visitAlterStatementSuffixSetPartSpec(self, ctx:HiveParser.AlterStatementSuffixSetPartSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterStatementSuffixExecute.
    def visitAlterStatementSuffixExecute(self, ctx:HiveParser.AlterStatementSuffixExecuteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#fileFormat.
    def visitFileFormat(self, ctx:HiveParser.FileFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterDataConnectorStatementSuffix.
    def visitAlterDataConnectorStatementSuffix(self, ctx:HiveParser.AlterDataConnectorStatementSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterDataConnectorSuffixProperties.
    def visitAlterDataConnectorSuffixProperties(self, ctx:HiveParser.AlterDataConnectorSuffixPropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterDataConnectorSuffixSetOwner.
    def visitAlterDataConnectorSuffixSetOwner(self, ctx:HiveParser.AlterDataConnectorSuffixSetOwnerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterDataConnectorSuffixSetUrl.
    def visitAlterDataConnectorSuffixSetUrl(self, ctx:HiveParser.AlterDataConnectorSuffixSetUrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#likeTableOrFile.
    def visitLikeTableOrFile(self, ctx:HiveParser.LikeTableOrFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createTableStatement.
    def visitCreateTableStatement(self, ctx:HiveParser.CreateTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createDataConnectorStatement.
    def visitCreateDataConnectorStatement(self, ctx:HiveParser.CreateDataConnectorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dataConnectorComment.
    def visitDataConnectorComment(self, ctx:HiveParser.DataConnectorCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dataConnectorUrl.
    def visitDataConnectorUrl(self, ctx:HiveParser.DataConnectorUrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dataConnectorType.
    def visitDataConnectorType(self, ctx:HiveParser.DataConnectorTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dcProperties.
    def visitDcProperties(self, ctx:HiveParser.DcPropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropDataConnectorStatement.
    def visitDropDataConnectorStatement(self, ctx:HiveParser.DropDataConnectorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableAllColumns.
    def visitTableAllColumns(self, ctx:HiveParser.TableAllColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableOrColumn.
    def visitTableOrColumn(self, ctx:HiveParser.TableOrColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableDotColumn.
    def visitTableDotColumn(self, ctx:HiveParser.TableDotColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#defaultValue.
    def visitDefaultValue(self, ctx:HiveParser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#expressionList.
    def visitExpressionList(self, ctx:HiveParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#aliasList.
    def visitAliasList(self, ctx:HiveParser.AliasListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#fromClause.
    def visitFromClause(self, ctx:HiveParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#fromSource.
    def visitFromSource(self, ctx:HiveParser.FromSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#atomjoinSource.
    def visitAtomjoinSource(self, ctx:HiveParser.AtomjoinSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#joinSource.
    def visitJoinSource(self, ctx:HiveParser.JoinSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#otherjoinSource.
    def visitOtherjoinSource(self, ctx:HiveParser.OtherjoinSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#joinSourcePart.
    def visitJoinSourcePart(self, ctx:HiveParser.JoinSourcePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#uniqueJoinSource.
    def visitUniqueJoinSource(self, ctx:HiveParser.UniqueJoinSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#uniqueJoinExpr.
    def visitUniqueJoinExpr(self, ctx:HiveParser.UniqueJoinExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#uniqueJoinToken.
    def visitUniqueJoinToken(self, ctx:HiveParser.UniqueJoinTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#joinToken.
    def visitJoinToken(self, ctx:HiveParser.JoinTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#lateralView.
    def visitLateralView(self, ctx:HiveParser.LateralViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableAlias.
    def visitTableAlias(self, ctx:HiveParser.TableAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableBucketSample.
    def visitTableBucketSample(self, ctx:HiveParser.TableBucketSampleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#splitSample.
    def visitSplitSample(self, ctx:HiveParser.SplitSampleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableSample.
    def visitTableSample(self, ctx:HiveParser.TableSampleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableSource.
    def visitTableSource(self, ctx:HiveParser.TableSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#asOfClause.
    def visitAsOfClause(self, ctx:HiveParser.AsOfClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#uniqueJoinTableSource.
    def visitUniqueJoinTableSource(self, ctx:HiveParser.UniqueJoinTableSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableName.
    def visitTableName(self, ctx:HiveParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#viewName.
    def visitViewName(self, ctx:HiveParser.ViewNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#subQuerySource.
    def visitSubQuerySource(self, ctx:HiveParser.SubQuerySourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partitioningSpec.
    def visitPartitioningSpec(self, ctx:HiveParser.PartitioningSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partitionTableFunctionSource.
    def visitPartitionTableFunctionSource(self, ctx:HiveParser.PartitionTableFunctionSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partitionedTableFunction.
    def visitPartitionedTableFunction(self, ctx:HiveParser.PartitionedTableFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#whereClause.
    def visitWhereClause(self, ctx:HiveParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#searchCondition.
    def visitSearchCondition(self, ctx:HiveParser.SearchConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#valuesSource.
    def visitValuesSource(self, ctx:HiveParser.ValuesSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#valuesClause.
    def visitValuesClause(self, ctx:HiveParser.ValuesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#valuesTableConstructor.
    def visitValuesTableConstructor(self, ctx:HiveParser.ValuesTableConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#valueRowConstructor.
    def visitValueRowConstructor(self, ctx:HiveParser.ValueRowConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#firstValueRowConstructor.
    def visitFirstValueRowConstructor(self, ctx:HiveParser.FirstValueRowConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#virtualTableSource.
    def visitVirtualTableSource(self, ctx:HiveParser.VirtualTableSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#selectClause.
    def visitSelectClause(self, ctx:HiveParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#all_distinct.
    def visitAll_distinct(self, ctx:HiveParser.All_distinctContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#selectList.
    def visitSelectList(self, ctx:HiveParser.SelectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#selectTrfmClause.
    def visitSelectTrfmClause(self, ctx:HiveParser.SelectTrfmClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#selectItem.
    def visitSelectItem(self, ctx:HiveParser.SelectItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#trfmClause.
    def visitTrfmClause(self, ctx:HiveParser.TrfmClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#selectExpression.
    def visitSelectExpression(self, ctx:HiveParser.SelectExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#selectExpressionList.
    def visitSelectExpressionList(self, ctx:HiveParser.SelectExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#window_clause.
    def visitWindow_clause(self, ctx:HiveParser.Window_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#window_defn.
    def visitWindow_defn(self, ctx:HiveParser.Window_defnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#window_specification.
    def visitWindow_specification(self, ctx:HiveParser.Window_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#window_frame.
    def visitWindow_frame(self, ctx:HiveParser.Window_frameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#window_range_expression.
    def visitWindow_range_expression(self, ctx:HiveParser.Window_range_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#window_value_expression.
    def visitWindow_value_expression(self, ctx:HiveParser.Window_value_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#window_frame_start_boundary.
    def visitWindow_frame_start_boundary(self, ctx:HiveParser.Window_frame_start_boundaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#window_frame_boundary.
    def visitWindow_frame_boundary(self, ctx:HiveParser.Window_frame_boundaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#groupByClause.
    def visitGroupByClause(self, ctx:HiveParser.GroupByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#groupby_expression.
    def visitGroupby_expression(self, ctx:HiveParser.Groupby_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#groupByEmpty.
    def visitGroupByEmpty(self, ctx:HiveParser.GroupByEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#rollupStandard.
    def visitRollupStandard(self, ctx:HiveParser.RollupStandardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#rollupOldSyntax.
    def visitRollupOldSyntax(self, ctx:HiveParser.RollupOldSyntaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#groupingSetExpression.
    def visitGroupingSetExpression(self, ctx:HiveParser.GroupingSetExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#groupingSetExpressionMultiple.
    def visitGroupingSetExpressionMultiple(self, ctx:HiveParser.GroupingSetExpressionMultipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#groupingExpressionSingle.
    def visitGroupingExpressionSingle(self, ctx:HiveParser.GroupingExpressionSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#havingClause.
    def visitHavingClause(self, ctx:HiveParser.HavingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#qualifyClause.
    def visitQualifyClause(self, ctx:HiveParser.QualifyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#havingCondition.
    def visitHavingCondition(self, ctx:HiveParser.HavingConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#expressionsInParenthesis.
    def visitExpressionsInParenthesis(self, ctx:HiveParser.ExpressionsInParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#expressionsNotInParenthesis.
    def visitExpressionsNotInParenthesis(self, ctx:HiveParser.ExpressionsNotInParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#expressionPart.
    def visitExpressionPart(self, ctx:HiveParser.ExpressionPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#expressionOrDefault.
    def visitExpressionOrDefault(self, ctx:HiveParser.ExpressionOrDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#firstExpressionsWithAlias.
    def visitFirstExpressionsWithAlias(self, ctx:HiveParser.FirstExpressionsWithAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#expressionWithAlias.
    def visitExpressionWithAlias(self, ctx:HiveParser.ExpressionWithAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#expressions.
    def visitExpressions(self, ctx:HiveParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnRefOrderInParenthesis.
    def visitColumnRefOrderInParenthesis(self, ctx:HiveParser.ColumnRefOrderInParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#columnRefOrderNotInParenthesis.
    def visitColumnRefOrderNotInParenthesis(self, ctx:HiveParser.ColumnRefOrderNotInParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#orderByClause.
    def visitOrderByClause(self, ctx:HiveParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#clusterByClause.
    def visitClusterByClause(self, ctx:HiveParser.ClusterByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partitionByClause.
    def visitPartitionByClause(self, ctx:HiveParser.PartitionByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#distributeByClause.
    def visitDistributeByClause(self, ctx:HiveParser.DistributeByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#sortByClause.
    def visitSortByClause(self, ctx:HiveParser.SortByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#trimFunction.
    def visitTrimFunction(self, ctx:HiveParser.TrimFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#function_.
    def visitFunction_(self, ctx:HiveParser.Function_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#null_treatment.
    def visitNull_treatment(self, ctx:HiveParser.Null_treatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#functionName.
    def visitFunctionName(self, ctx:HiveParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#castExpression.
    def visitCastExpression(self, ctx:HiveParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#caseExpression.
    def visitCaseExpression(self, ctx:HiveParser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#whenExpression.
    def visitWhenExpression(self, ctx:HiveParser.WhenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#floorExpression.
    def visitFloorExpression(self, ctx:HiveParser.FloorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#floorDateQualifiers.
    def visitFloorDateQualifiers(self, ctx:HiveParser.FloorDateQualifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#extractExpression.
    def visitExtractExpression(self, ctx:HiveParser.ExtractExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#timeQualifiers.
    def visitTimeQualifiers(self, ctx:HiveParser.TimeQualifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#constant.
    def visitConstant(self, ctx:HiveParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#prepareStmtParam.
    def visitPrepareStmtParam(self, ctx:HiveParser.PrepareStmtParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#parameterIdx.
    def visitParameterIdx(self, ctx:HiveParser.ParameterIdxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#stringLiteralSequence.
    def visitStringLiteralSequence(self, ctx:HiveParser.StringLiteralSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#charSetStringLiteral.
    def visitCharSetStringLiteral(self, ctx:HiveParser.CharSetStringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dateLiteral.
    def visitDateLiteral(self, ctx:HiveParser.DateLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#timestampLiteral.
    def visitTimestampLiteral(self, ctx:HiveParser.TimestampLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#timestampLocalTZLiteral.
    def visitTimestampLocalTZLiteral(self, ctx:HiveParser.TimestampLocalTZLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#intervalValue.
    def visitIntervalValue(self, ctx:HiveParser.IntervalValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#intervalLiteral.
    def visitIntervalLiteral(self, ctx:HiveParser.IntervalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#intervalExpression.
    def visitIntervalExpression(self, ctx:HiveParser.IntervalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#intervalQualifiers.
    def visitIntervalQualifiers(self, ctx:HiveParser.IntervalQualifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#expression.
    def visitExpression(self, ctx:HiveParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#atomExpression.
    def visitAtomExpression(self, ctx:HiveParser.AtomExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceFieldExpression.
    def visitPrecedenceFieldExpression(self, ctx:HiveParser.PrecedenceFieldExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceUnaryOperator.
    def visitPrecedenceUnaryOperator(self, ctx:HiveParser.PrecedenceUnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceUnaryPrefixExpression.
    def visitPrecedenceUnaryPrefixExpression(self, ctx:HiveParser.PrecedenceUnaryPrefixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceBitwiseXorOperator.
    def visitPrecedenceBitwiseXorOperator(self, ctx:HiveParser.PrecedenceBitwiseXorOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceBitwiseXorExpression.
    def visitPrecedenceBitwiseXorExpression(self, ctx:HiveParser.PrecedenceBitwiseXorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceStarOperator.
    def visitPrecedenceStarOperator(self, ctx:HiveParser.PrecedenceStarOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceStarExpression.
    def visitPrecedenceStarExpression(self, ctx:HiveParser.PrecedenceStarExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedencePlusOperator.
    def visitPrecedencePlusOperator(self, ctx:HiveParser.PrecedencePlusOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedencePlusExpression.
    def visitPrecedencePlusExpression(self, ctx:HiveParser.PrecedencePlusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceConcatenateOperator.
    def visitPrecedenceConcatenateOperator(self, ctx:HiveParser.PrecedenceConcatenateOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceConcatenateExpression.
    def visitPrecedenceConcatenateExpression(self, ctx:HiveParser.PrecedenceConcatenateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceAmpersandOperator.
    def visitPrecedenceAmpersandOperator(self, ctx:HiveParser.PrecedenceAmpersandOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceAmpersandExpression.
    def visitPrecedenceAmpersandExpression(self, ctx:HiveParser.PrecedenceAmpersandExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceBitwiseOrOperator.
    def visitPrecedenceBitwiseOrOperator(self, ctx:HiveParser.PrecedenceBitwiseOrOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceBitwiseOrExpression.
    def visitPrecedenceBitwiseOrExpression(self, ctx:HiveParser.PrecedenceBitwiseOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceRegexpOperator.
    def visitPrecedenceRegexpOperator(self, ctx:HiveParser.PrecedenceRegexpOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceSimilarOperator.
    def visitPrecedenceSimilarOperator(self, ctx:HiveParser.PrecedenceSimilarOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#subQueryExpression.
    def visitSubQueryExpression(self, ctx:HiveParser.SubQueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceSimilarExpression.
    def visitPrecedenceSimilarExpression(self, ctx:HiveParser.PrecedenceSimilarExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceSimilarExpressionMain.
    def visitPrecedenceSimilarExpressionMain(self, ctx:HiveParser.PrecedenceSimilarExpressionMainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceSimilarExpressionPart.
    def visitPrecedenceSimilarExpressionPart(self, ctx:HiveParser.PrecedenceSimilarExpressionPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceSimilarExpressionAtom.
    def visitPrecedenceSimilarExpressionAtom(self, ctx:HiveParser.PrecedenceSimilarExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceSimilarExpressionQuantifierPredicate.
    def visitPrecedenceSimilarExpressionQuantifierPredicate(self, ctx:HiveParser.PrecedenceSimilarExpressionQuantifierPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#quantifierType.
    def visitQuantifierType(self, ctx:HiveParser.QuantifierTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceSimilarExpressionIn.
    def visitPrecedenceSimilarExpressionIn(self, ctx:HiveParser.PrecedenceSimilarExpressionInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceSimilarExpressionPartNot.
    def visitPrecedenceSimilarExpressionPartNot(self, ctx:HiveParser.PrecedenceSimilarExpressionPartNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceDistinctOperator.
    def visitPrecedenceDistinctOperator(self, ctx:HiveParser.PrecedenceDistinctOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceEqualOperator.
    def visitPrecedenceEqualOperator(self, ctx:HiveParser.PrecedenceEqualOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceEqualExpression.
    def visitPrecedenceEqualExpression(self, ctx:HiveParser.PrecedenceEqualExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#isCondition.
    def visitIsCondition(self, ctx:HiveParser.IsConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceUnarySuffixExpression.
    def visitPrecedenceUnarySuffixExpression(self, ctx:HiveParser.PrecedenceUnarySuffixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceNotOperator.
    def visitPrecedenceNotOperator(self, ctx:HiveParser.PrecedenceNotOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceNotExpression.
    def visitPrecedenceNotExpression(self, ctx:HiveParser.PrecedenceNotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceAndOperator.
    def visitPrecedenceAndOperator(self, ctx:HiveParser.PrecedenceAndOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceAndExpression.
    def visitPrecedenceAndExpression(self, ctx:HiveParser.PrecedenceAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceOrOperator.
    def visitPrecedenceOrOperator(self, ctx:HiveParser.PrecedenceOrOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#precedenceOrExpression.
    def visitPrecedenceOrExpression(self, ctx:HiveParser.PrecedenceOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#booleanValue.
    def visitBooleanValue(self, ctx:HiveParser.BooleanValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#booleanValueTok.
    def visitBooleanValueTok(self, ctx:HiveParser.BooleanValueTokContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#tableOrPartition.
    def visitTableOrPartition(self, ctx:HiveParser.TableOrPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partitionSpec.
    def visitPartitionSpec(self, ctx:HiveParser.PartitionSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partitionVal.
    def visitPartitionVal(self, ctx:HiveParser.PartitionValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partitionSelectorSpec.
    def visitPartitionSelectorSpec(self, ctx:HiveParser.PartitionSelectorSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partitionSelectorVal.
    def visitPartitionSelectorVal(self, ctx:HiveParser.PartitionSelectorValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#partitionSelectorOperator.
    def visitPartitionSelectorOperator(self, ctx:HiveParser.PartitionSelectorOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#subQuerySelectorOperator.
    def visitSubQuerySelectorOperator(self, ctx:HiveParser.SubQuerySelectorOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#sysFuncNames.
    def visitSysFuncNames(self, ctx:HiveParser.SysFuncNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#descFuncNames.
    def visitDescFuncNames(self, ctx:HiveParser.DescFuncNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#id_.
    def visitId_(self, ctx:HiveParser.Id_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#functionIdentifier.
    def visitFunctionIdentifier(self, ctx:HiveParser.FunctionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#principalIdentifier.
    def visitPrincipalIdentifier(self, ctx:HiveParser.PrincipalIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#nonReserved.
    def visitNonReserved(self, ctx:HiveParser.NonReservedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#sql11ReservedKeywordsUsedAsFunctionName.
    def visitSql11ReservedKeywordsUsedAsFunctionName(self, ctx:HiveParser.Sql11ReservedKeywordsUsedAsFunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#hint.
    def visitHint(self, ctx:HiveParser.HintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#hintList.
    def visitHintList(self, ctx:HiveParser.HintListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#hintItem.
    def visitHintItem(self, ctx:HiveParser.HintItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#hintName.
    def visitHintName(self, ctx:HiveParser.HintNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#hintArgs.
    def visitHintArgs(self, ctx:HiveParser.HintArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#hintArgName.
    def visitHintArgName(self, ctx:HiveParser.HintArgNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#prepareStatement.
    def visitPrepareStatement(self, ctx:HiveParser.PrepareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#executeStatement.
    def visitExecuteStatement(self, ctx:HiveParser.ExecuteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#executeParamList.
    def visitExecuteParamList(self, ctx:HiveParser.ExecuteParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#resourcePlanDdlStatements.
    def visitResourcePlanDdlStatements(self, ctx:HiveParser.ResourcePlanDdlStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#rpAssign.
    def visitRpAssign(self, ctx:HiveParser.RpAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#rpAssignList.
    def visitRpAssignList(self, ctx:HiveParser.RpAssignListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#rpUnassign.
    def visitRpUnassign(self, ctx:HiveParser.RpUnassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#rpUnassignList.
    def visitRpUnassignList(self, ctx:HiveParser.RpUnassignListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createResourcePlanStatement.
    def visitCreateResourcePlanStatement(self, ctx:HiveParser.CreateResourcePlanStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#withReplace.
    def visitWithReplace(self, ctx:HiveParser.WithReplaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#activate.
    def visitActivate(self, ctx:HiveParser.ActivateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#enable.
    def visitEnable(self, ctx:HiveParser.EnableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#disable.
    def visitDisable(self, ctx:HiveParser.DisableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#unmanaged.
    def visitUnmanaged(self, ctx:HiveParser.UnmanagedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterResourcePlanStatement.
    def visitAlterResourcePlanStatement(self, ctx:HiveParser.AlterResourcePlanStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#globalWmStatement.
    def visitGlobalWmStatement(self, ctx:HiveParser.GlobalWmStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#replaceResourcePlanStatement.
    def visitReplaceResourcePlanStatement(self, ctx:HiveParser.ReplaceResourcePlanStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropResourcePlanStatement.
    def visitDropResourcePlanStatement(self, ctx:HiveParser.DropResourcePlanStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#poolPath.
    def visitPoolPath(self, ctx:HiveParser.PoolPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#triggerExpression.
    def visitTriggerExpression(self, ctx:HiveParser.TriggerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#triggerExpressionStandalone.
    def visitTriggerExpressionStandalone(self, ctx:HiveParser.TriggerExpressionStandaloneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#triggerOrExpression.
    def visitTriggerOrExpression(self, ctx:HiveParser.TriggerOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#triggerAndExpression.
    def visitTriggerAndExpression(self, ctx:HiveParser.TriggerAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#triggerAtomExpression.
    def visitTriggerAtomExpression(self, ctx:HiveParser.TriggerAtomExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#triggerLiteral.
    def visitTriggerLiteral(self, ctx:HiveParser.TriggerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#comparisionOperator.
    def visitComparisionOperator(self, ctx:HiveParser.ComparisionOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#triggerActionExpression.
    def visitTriggerActionExpression(self, ctx:HiveParser.TriggerActionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#triggerActionExpressionStandalone.
    def visitTriggerActionExpressionStandalone(self, ctx:HiveParser.TriggerActionExpressionStandaloneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createTriggerStatement.
    def visitCreateTriggerStatement(self, ctx:HiveParser.CreateTriggerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterTriggerStatement.
    def visitAlterTriggerStatement(self, ctx:HiveParser.AlterTriggerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropTriggerStatement.
    def visitDropTriggerStatement(self, ctx:HiveParser.DropTriggerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#poolAssign.
    def visitPoolAssign(self, ctx:HiveParser.PoolAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#poolAssignList.
    def visitPoolAssignList(self, ctx:HiveParser.PoolAssignListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createPoolStatement.
    def visitCreatePoolStatement(self, ctx:HiveParser.CreatePoolStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterPoolStatement.
    def visitAlterPoolStatement(self, ctx:HiveParser.AlterPoolStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropPoolStatement.
    def visitDropPoolStatement(self, ctx:HiveParser.DropPoolStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#createMappingStatement.
    def visitCreateMappingStatement(self, ctx:HiveParser.CreateMappingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#alterMappingStatement.
    def visitAlterMappingStatement(self, ctx:HiveParser.AlterMappingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HiveParser#dropMappingStatement.
    def visitDropMappingStatement(self, ctx:HiveParser.DropMappingStatementContext):
        return self.visitChildren(ctx)



del HiveParser