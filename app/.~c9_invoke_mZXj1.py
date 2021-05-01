from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory, PromotionDrinkMD, HealthDrinkMD, AlcoholicBeveragesMD, Alldrinks, Food, Foodsnack, FoodConfectionery, AllShop, ShopType, TypeOfProduct, SeaFood, Fish, Meat
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']
    
#admin 內容
class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']
    
class NewsPageView(BaseView):
    default_view = 'local_news'
    

    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News1234'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/global_news/')
    def global_news(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)
#KCY
class PromotionDrinkView(ModelView):
    datamodel = SQLAInterface(PromotionDrinkMD)
    list_columns = ['id', 'title', 'content', 'price']
    
class HealthDrinkView(ModelView):
    datamodel = SQLAInterface(HealthDrinkMD)
    list_columns = ['id', 'title', 'content', 'price']
    
class AlcoholicBeveragesView(ModelView):
    datamodel = SQLAInterface(AlcoholicBeveragesMD)
    list_columns = ['id', 'title', 'content', 'price']
    
class AlldrinksView(ModelView):
    datamodel = SQLAInterface(Alldrinks)
    list_columns = ['id', 'title', 'cat_id']

#HIN try
class FoodView(ModelView):
    datamodel = SQLAInterface(Food)
    list_columns = ['id', 'title', 'name', 'Price','Food_type']

class FoodsnackView(ModelView):
    datamodel = SQLAInterface(Foodsnack)
    list_columns = ['id', 'title', 'name', 'Price']
    
class FoodConfectioneryView(ModelView):
    datamodel = SQLAInterface(FoodConfectionery)
    list_columns = ['id', 'title', 'name', 'Price']
    
class FoodPageView(BaseView):
    default_view = 'Biscuits'
 
    @expose('/Biscuits/')
    def Biscuits(self):
        param1 = 'Biscuits'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)
        
    @expose('/Snacks/')
    def Snacks(self):
        param1 = 'Snacks'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)
        
    @expose('/Confectionery/')
    def Confectionery(self):
        param1 = 'Confectionery'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)
 
#Li try
class SeaFoodView(ModelView):
    datamodel = SQLAInterface(SeaFood)
    list_columns = ['id', 'title', 'origin', 'Price']

class FishView(ModelView):
    datamodel = SQLAInterface(Fish)
    list_columns = ['id', 'title', 'origin', 'Price']

class MeatView(ModelView):
    datamodel = SQLAInterface(Meat)
    list_columns = ['id', 'title', 'origin', 'Price']


#HMK

class AllShopView(ModelView):
    datamodel = SQLAInterface(AllShop)
    list_columns = ['id', 'shop_area', 'shop_district', 'shop_type']

class ShopTypeView(ModelView):
    datamodel = SQLAInterface(ShopType)
    list_columns = ['id', 'shoptype_name']

class TypeOfProductView(ModelView):
    datamodel = SQLAInterface(TypeOfProduct)
    list_columns = ['id', 'type_name']
    
   
    

db.create_all()
#KCY Review
appbuilder.add_view(PromotionDrinkView, "PromotionDrink", category="Drinks")
appbuilder.add_view(HealthDrinkView, "HealthDrink", category="Drinks")
appbuilder.add_view(AlcoholicBeveragesView, "AlcoholicBeverages", category="Drinks")
appbuilder.add_view(AlldrinksView, "Alldrinks", category="Drinks")

#hin try
appbuilder.add_view(FoodView, 'Biscuits', category="Food")
appbuilder.add_view(FoodsnackView, 'Snacks', category="Food")
appbuilder.add_view(FoodConfectioneryView, 'Confectionery', category="Food")

#Li try
appbuilder.add_view(SeaFoodView, 'SeaFood', category="FrozenFood")
appbuilder.add_view(FishView, 'Fish', category="FrozenFood")
appbuilder.add_view(MeatView, 'Meat', category="FrozenFood")

#HMK try
appbuilder.add_view(AllShopView, 'places', category='Shops')
appbuilder.add_view(ShopTypeView, 'Shop_type', category='Shops')
appbuilder.add_view(TypeOfProductView, 'Type', category='All type')





""" Page View """
appbuilder.add_view(NewsPageView, 'Local News', category="News")
appbuilder.add_link("Global News", href="/newspageview/global_news/", category="News")
""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")

