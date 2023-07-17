import flet as ft

def main(page: ft.Page):
    page.title = "Weight conv"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE

    weight_text_field = ft.TextField(
        label="Enter your weight",
        value="0",
        text_align=ft.TextAlign.CENTER,
        width=100,
        border_color= ft.colors.GREEN,
    )

    unit_text_field = ft.TextField(
        label="(K)g or (L)bs:", 
        text_align=ft.TextAlign.CENTER, 
        width=100
    )

    converted_text = ft.Text(
        ""
    )

    def convert_weight(e):
        weight_value = float(weight_text_field.value)

        if unit_text_field.value.upper() == 'K':
            converted_value = weight_value / 0.45
            converted_text.value = 'Weight in lbs is: ' + str(converted_value)
        else: 
            converted_value = weight_value * 0.45
            converted_text.value = 'Weight in kgs: ' + str(converted_value)
            
        page.update()
    

    page.add(
        ft.Row(
            [
                weight_text_field,
                unit_text_field,
                ft.IconButton(
                    ft.icons.CHANGE_CIRCLE, 
                    on_click=convert_weight,
                ),
                converted_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
