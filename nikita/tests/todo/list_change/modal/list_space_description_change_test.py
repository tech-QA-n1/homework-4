from nikita.tests.todo.list_change.default import ListChangeTest
from nikita.pages.todo.list import ListPage

class ListSpaceDescriptionChangeTest(ListChangeTest):
    DESCRIPTION = '   '

    def test(self):
        page = ListPage(self.driver)
        page.change_description_modal(self.DESCRIPTION)
        page.wait_for_description(self.DESCRIPTION)
