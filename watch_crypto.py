import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import ccxt
from time import gmtime, strftime

kraken = ccxt.kraken()
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def tik_tak():
    saat = strftime("%H", gmtime())
    yerel_saat = str(int(saat) + 1)
    dakika = strftime("%M", gmtime())
    saniye = strftime("%S", gmtime())
    zaman = f"{yerel_saat}{dakika}{saniye}"
    a = int(zaman)
    return a

def fiyat():
    for trade in kraken.fetch_trades('BTC/EUR'):
        a = float(f"{trade['price']}")
        return a

xs = []
ys = []
ax1.clear()
def animate(i):
    y = float(fiyat())
    x = int(tik_tak())
    xs.append(x)
    ys.append(y)
    print(xs[:30], ys[:30])
    ax1.set_xlabel('Zaman', fontsize=12)
    ax1.set_ylabel('Fiyat/€', fontsize=12)
    ax1.plot(xs[:60], ys[:60])

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
