from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='income' ),
    path('add-income', views.add_income , name='add-income' ),
    path('edit-income/<int:id>', views.income_edit , name='edit-income' ),
    path('income-delete/<int:id>', views.delete_income , name='income-delete' ),
    path('income_catogory_summary', views.income_catogory_summary, name="income_catogory_summary"),

    path('incomeStats', views.income_stats_view , name='incomeStats' ),
]

    

