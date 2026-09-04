import random
import discord
import os
import time
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def mem(ctx):
    files=os.listdir('images')
    selected = random.choice(files)

    with open(f'images/{selected}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, get_duck_image_url fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    '''dog komutunu çağırdığımızda, get_dog_image_url fonksiyonunu çağırır.'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def recyclable(ctx):
    await ctx.send(f'İşte bazı geri dönüştürülebilir malzemeler: Kağıt, Karton, Cam, Plastik, Metal, Elektronik atıklar, Piller, Giysiler ve Tekstil ürünleri. Lütfen geri dönüşüm kutularına atmayı unutmayın!')

@bot.command()
async def biodegrade(ctx):
    await ctx.send(f'Plastik: 100-1000 yıl, Cam: 1 milyon yıl, Alüminyum kutular: 200-500 yıl, Kağıt: 2-6 hafta, Organik atıklar: 1-6 ay, Tekstil ürünleri: 1-5 yıl, Elektronik atıklar: 10-50 yıl. Lütfen geri dönüşüm ve atık yönetimine dikkat edelim!')

@bot.command()
async def recyclebins(ctx):
    await ctx.send(f'İşte bazı geri dönüşüm kutusu renkleri ve anlamları: Mavi: Kağıt ve karton, Yeşil: Cam, Sarı: Plastik ve metal, Kahverengi: Organik atıklar, Gri/Siyah: Genel atık. Lütfen atıkları doğru kutulara atmayı unutmayın!')

@bot.command()
async def is_recycle_important(ctx):
    await ctx.send(f'Evet, geri dönüşüm çok önemlidir! Geri dönüşüm, doğal kaynakları korumamıza, enerji tasarrufu yapmamıza ve çevre kirliliğini azaltmamıza yardımcı olur. Ayrıca, atıkların geri dönüştürülmesi, yeni ürünlerin üretiminde kullanılabilecek malzemelerin elde edilmesini sağlar. Bu nedenle, geri dönüşüm alışkanlıklarını benimsemek ve atıkları doğru şekilde ayrıştırmak büyük bir fark yaratabilir!')

@bot.command()
async def reuse(ctx):
    await ctx.send(f'Yeniden kullanım da geri dönüşüm kadar önemlidir! Yeniden kullanım, atıkların tekrar kullanılmasını ve böylece doğal kaynakların korunmasını sağlar. Örneğin, cam kavanozları veya plastik şişeleri tekrar kullanmak, kağıt torbaları veya kutuları yeniden değerlendirmek gibi basit adımlar, çevreye büyük katkı sağlayabilir. Ayrıca, yeniden kullanım, atık miktarını azaltarak çöp sahalarının dolmasını önler ve enerji tasarrufu sağlar. Bu nedenle, yeniden kullanım alışkanlıklarını benimsemek ve atıkları mümkün olduğunca tekrar kullanmak önemlidir!')

@bot.command()
async def plastic(ctx):
    await ctx.send(f"Demek plastik hakkında birşeyler öğrenmek ve geri dönüşüm yapmak istiyorsun. Tamam o zaman anlatıyorum.")
    time.sleep(2)
    await ctx.send(f"Plastik doğada çok uzun yıllar boyunca çözülmeden kalabilir. Örneğin bir plastik şişe 450+ yıla kadar doğada çözünmeden kalabilir.")
    time.sleep(2)
    await ctx.send(f"Plastikler toprağa,yeraltı sularına ve denizlere karışabilir. Bu bölgede yaşayan canlıları da tehlikeye sokar.")
    time.sleep(2)
    await ctx.send(f"Örneğin deniz kaplumbağaları plastik poşetleri denizanası sanarak yutar ve boğulur.")
    time.sleep(2)
    await ctx.send(f"Başka bir örnek olarak ise deniz kuşları ve balıkların mideleri plastik atıklarla dolarak açlıktan ölmelerine neden olur.")

@bot.command()
async def commands(ctx):
    await ctx.send(f'İşte kullanabileceğiniz tüm komutlar : !hello , !heh , !repeat , !gen_pass , !emoji_olusturucu, !choose , !mem , !duck , !dog , !commands , !recyclable , !biodegrade , !recyclebins , !is_recycle_important ,!reuse , !commands_about_recycle, !plastic')

@bot.command()
async def commands_about_enviroment(ctx):
    await ctx.send(f'İşte kullanabileceğiniz bazı komutlar :  !recyclable , !biodegrade , !recyclebins , !is_recycle_important , !reuse , !plastic')
    
bot.run("Write your token here !")
