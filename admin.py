from . import models
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("todolist,  "created", "due_date")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Category, CategoryAdmin)