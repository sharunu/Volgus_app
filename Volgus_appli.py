# -*- coding: utf-8 -*-
import tkinter
import Volgus_Thunder



class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=380, height=280,
                         borderwidth=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()



    def create_widgets(self):
        # 閉じるボタン
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '閉じる'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side='bottom')

        label = tkinter.Label(self, text='入力')
        label.pack(padx=100,pady=0)

        label = tkinter.Label(self, text='算出生物数下限')
        label.place(relx=0.1,rely=0.1)

        label = tkinter.Label(self, text='算出生物数上限')
        label.place(relx=0.1,rely=0.2)

        label = tkinter.Label(self, text='試行回数')
        label.place(relx=0.1,rely=0.3)

        label = tkinter.Label(self, text='デッキ枚数')
        label.place(relx=0.1,rely=0.4)


        # テキストボックス
        self.hikoukai = tkinter.Entry(self)
        self.hikoukai['width'] = 10
        self.hikoukai.pack()

        self.zan_st = tkinter.Entry(self)
        self.zan_st['width'] = 10
        self.zan_st.pack()

        self.shield = tkinter.Entry(self)
        self.shield['width'] = 10
        self.shield.pack()

        self.need_st = tkinter.Entry(self)
        self.need_st['width'] = 10
        self.need_st.pack()



        # 実行ボタン
        submit_btn = tkinter.Button(self)
        submit_btn['text'] = '実行'
        submit_btn['command'] = self.input_handler
        submit_btn.pack()

        # メッセージ出力
        self.message = tkinter.Message(self)
        self.message.pack()

        #入力
    def input_handler(self):
        a = self.hikoukai.get()
        b = self.zan_st.get()
        c = self.shield.get()
        d = self.need_st.get()
        X = [a,b,c,d]
        text=Volgus_Thunder.tax(X)
        self.message['text'] = text 

        


root = tkinter.Tk()
root.title('ヴォルグサンダー計算機')
root.geometry('400x300')
app = Application(root=root)
app.mainloop()
