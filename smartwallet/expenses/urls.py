from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='expenses' ),
    path('add-expense/', views.add_expense , name='add-expenses' ),
    path('edit-expense/<int:id>', views.expense_edit , name='expense-edit' ),
    path('expense-delete/<int:id>', views.delete_expense , name='expense-delete' ),
    
    path('expense_catogory_summary', views.expense_catogory_summary, name="expense_catogory_summary"),
    path('stats', views.stats_view , name='stats' ),
]
