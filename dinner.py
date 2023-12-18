import flet as ft
import random

def __view__():

    def main(page:ft.Page):
        plat1 = ["Loubia", "Fries & Kafta", "Azghal", "Couscous Krorab", "Lentils"]
        plat2 = ["Macarona", "Couscous Veggie", "Couscous Tfaya", "Harira", "Batata Zitoun"]
        plat3 = ["Spaghetti", "Karane", "Byriani", "Hartita Bsal", "Rice Salad"]
        plat1.extend(plat2)   
        plat1.extend(plat3)
        entry1 = ft.TextField(label= "Today`s Dinner is : ", value="",width =400, border_color="#E95793")
        entry2 = ft.TextField(label="Add a Dish", width = 400, border_color="#E95793")

        def add_dish(item):
                item = entry2.value          
                plat1.append(item)
                entry2.value=""
                page.update()
        def today(dinner):
            dinner = random.choice(plat1)
            entry1.value= dinner
            page.update()

        add_btn = ft.ElevatedButton(text="Add New Dish",icon= ft.icons.ADD ,
                                    on_click= add_dish)
        rand_btn = ft.ElevatedButton(text="Today`s Dinner", icon= ft.icons.REFRESH , on_click=today)
        


        row1 = ft.Row(controls=[add_btn], alignment= ft.MainAxisAlignment.CENTER)
        row2 = ft.Row(controls=[rand_btn], alignment= ft.MainAxisAlignment.CENTER)
        page.update()
        page.window_width =400
        page.window_height=400
        page.title="What`s For Dinner ?"
        #page.bgcolor = "white"
        #page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.add(entry1, entry2, row1, row2)



    ft.app(target=main, view= ft.WEB_BROWSER)