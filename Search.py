import Tkinter
from googlesearch import search


def smartsearch():
    query = "site:Linkedin.com intitle:Apple"
    my_results_list = []
    for i in search(query,
                    tld='com',
                    lang='en',
                    num=10,
                    start=0,
                    stop=None,
                    pause=2.0,
                    ):
        my_results_list.append(i)
        print(i)


top = Tkinter.Tk()
top.geometry("600x400")
L1 = Tkinter.Label(top, text="Website")
L1.pack( side = Tkinter.LEFT)
E1 = Tkinter.Entry(top, bd =5)
E1.pack(side = Tkinter.RIGHT)
L2 = Tkinter.Label(top, text="Search")
L2.pack( side = Tkinter.LEFT)
E2 = Tkinter.Entry(top, bd =5)
E2.pack(side = Tkinter.RIGHT)
top.mainloop()
