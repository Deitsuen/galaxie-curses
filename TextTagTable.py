from TextTag import *




class TextTagTable(object):

    def __init__(self):
        self.Text_tag = TextTag()

        self.r =  self.Text_tag.text_tag_new('text')

    def text_table_tag_table_new(self):
        pass


    def text_tag_table_add(self):
         Text_tag_table = TextTagTable()
         tag =self.Text_tag.text_tag_new('text')
         table= Text_tag_table.text_table_tag_table_new()




if __name__ == '__main__':
    table = TextTagTable()
    print table.text_table_tag_table_new()
    print table.text_tag_table_add()
