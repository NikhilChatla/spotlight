from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()

urlpatterns = [
    path('',include(router.urls)),
    path('database/',views.databaseView.as_view(),name='databaseView'),
    path('createTable/',views.createTableView.as_view(),name='createTable'),
    path('uploaded_list/',views.uploadView.as_view(),name='uploaded_list'),
    path('uploaded_list/<int:pk>',views.UploadLayerView.as_view()),
    path('dataQualityCheck/',views.dataQualityCheck.as_view(),name='dataQualityCheck-create'),
    path('getSchemaStructure/',views.getSchemaStructure.as_view(),name='getSchemaStructure'),
    path('getSchemaData/',views.getSchemaData.as_view(),name='getSchemaData'),
    path('getGoldLayerData/',views.goldLayerDataView.as_view(),name='goldLayerDataView'),
    path('goldDataPreview/',views.goldDataPreview.as_view(),name='goldDataPreview'),
    path('goldDataCreate/',views.goldDataCreate.as_view(),name='goldDataCreate'),
    path('project/',views.projectView.as_view(),name='projectView'),
    path('silvergoldtransform/',views.silverGoldTransformView.as_view(),name='silvergoldtansform'),
    path('bronzesilvertransform/',views.bronzeSilverTransform.as_view(),name='bronzeSilverTransform'),
    path('bronzeSilverInsert/',views.bronzeSilverInsert.as_view(),name='bronzeSilverInsert'),
    path('getSilverTable/<int:project_id>',views.getSilverTable.as_view(),name='getSilverTable'),
    path('getGoldTable/<str:table_name>',views.getGoldTable.as_view(),name='getGoldTable'),
    path('getSilverSchemaStructure/',views.getSilverSchemaStructure.as_view(),name='getSilverSchemaStructure'),
    path('getSilverSchemaColumn/',views.getSilverSchemaColumn.as_view(),name='getSilverSchemaColumn'),
    path('silverDataInsert/',views.silverDataInsert.as_view(),name='silverDataInsert'),
    path('getBronzeTable/',views.getBronzeTable.as_view(),name='getBronzeTable'),
    path('getBronzeSchemaColumn/',views.getBronzeSchemaStructure.as_view(),name='getBronzeSchemaStructure'),
    path('projectwithids/',views.projectDataSourceData.as_view(),name='projectDataSourceViewSet'),
    path('getSilverTableData/<str:table_name>',views.getSilverTableData.as_view()),
    path('getBronzeTableData/<str:table_name>',views.getBronzeTableData.as_view()),
    path('QueryLogs/',views.QueryLogsView.as_view(),name='QueryLogs'),
    path('dataTypeView/',views.dataTypeView.as_view(),name='dataTypeView'),
    path('alterTableSilver/',views.alterTableSilver.as_view(),name='alterTableSilver'),
    path('checkColumnSilverTable/',views.checkColumnSilverTable.as_view(),name='checkColumnSilverTable'),
    path('dataSource/<int:project_id>/<str:data_source>',views.DataSourceView.as_view()),
    path('getBronzeTableandColumns/<int:project_id>',views.getBronzeTableandColumns.as_view(), name='bronze_table_and_columns'),
    path('workflowrules/', views.worflowRulesView.as_view(), name='rules'),
    path('workflowrules/projectid/<int:project_id>', views.worflowRulesView.as_view(), name='worflowRulesView'),
    path('workflowrules/project_id/layer_id/<int:project_id>/<int:layer_id>', views.dataWithProject_RuleView.as_view(), name='worflowRulesView'),
    path('workflowrules/<int:id>', views.worflowRulesView.as_view(), name='rules'),
    path('layerdetails/',views.layerDetailsView.as_view(),name='layerDetailsView'),
    path('workflowTransition/',views.workflowTransitionView.as_view(),name='workflowTransitionView'),
    path('workflowTransition/project_id/<int:project_id>', views.workflowTransitionView.as_view(), name='workflowTransitionView'),
    path('getReportUrl/<int:project_id>',views.getReportUrl.as_view(), name='reportUrl'),
    path('audit/<int:project_id>',views.auditView.as_view(),name='auditView')
] 