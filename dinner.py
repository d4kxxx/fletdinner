import flet as ft
import random


async def main(page:ft.Page):
    page.title="Whats For Dinner"
    #page.window_height=500
    #page.window_width=500
    page.vertical_alignment= "center"
    page.horizontal_alignment="center"



    plat1 = ["Loubia", "Fries & Kafta", "Azghal", "Couscous Krorab", "Lentils"]
    plat2 = ["Macarona", "Couscous Veggie", "Couscous Tfaya", "Harira", "Batata Zitoun"]
    plat3 = ["Spaghetti", "Karane", "Byriani", "Hartita Bsal", "Rice Salad"]
    plat1.extend(plat2)   
    plat1.extend(plat3)
    entry1 = ft.TextField(label= "Today`s Dinner is : ", value="",width =400, border_color="#E95793")
    entry2 = ft.TextField(label="Add a Dish", width = 400, border_color="#E95793")

    async def add_dish(item):
            item = entry2.value          
            plat1.append(item)
            entry2.value=""
            await page.update_async()
    async def today(dinner):
        dinner = random.choice(plat1)
        entry1.value= dinner
        await page.update_async()

    add_btn = ft.ElevatedButton(text="Add New Dish",icon= ft.icons.ADD ,
                                on_click= add_dish)
    rand_btn = ft.ElevatedButton(text="Today`s Dinner", icon= ft.icons.REFRESH , on_click=today)
    

    text = ft.Text("Whats For Dinner Today ?", size=48)
    text1= ft.Text()
    row0 = ft.Row(controls=[text], alignment= ft.MainAxisAlignment.CENTER)
    row1 = ft.Row(controls=[add_btn], alignment= ft.MainAxisAlignment.CENTER)
    row2 = ft.Row(controls=[rand_btn], alignment= ft.MainAxisAlignment.CENTER)
    await page.update_async()
    
    
    
    await page.add_async(row0, text1, entry1, entry2, row1, row2)



ft.app(target=main, view=ft.WEB_BROWSER)