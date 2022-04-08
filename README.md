# 加密通话转换器

很多人会被查聊天记录，通常这种事情都让人抓狂。现在你可以用这个仓库里的程序和他人实现真正的“加密通话”，摆脱这种烦恼。

## 如何使用这个程序？

假如你安装了Python，你可以输入下面的指令安装：
```
pip install encrypted-chat
```

这个程序需要你和朋友一起运行，因此你们需要同时打开程序并在某一社交软件上在线。
你们需要约定好一个`g`与一个`p`（通常情况下可以设成两个大数字，但不宜超过10的50次方影响运行速度，最好是素数）。

举例如下（`g`和`p`太小了，不要学我）：
```
Welcome to encrypted chat.
Please enter your g-code: 5
Please enter your p-code: 97
```

然后，你会看到两个选项，此时选`1`发信，选`2`收信。（即一个加密一个解密）

如果选择发信模式，你会看到下面的内容：
```
Enter your option. 1 for encrypting, 2 for decrypting.
[Option] 1
(Ctrl+C to quit encrypting mode)
[Send] 46
Type what your target sent.
[Input]
```
此时对方（模式为`2`）也会看到这个界面（可能数字不同），此时**请让对方把你生成的数（即`[Send]`后面的一串数字）输入控制台**，同时，你输入对方生成的数。

现在我们假设对方向你发送了`19`，那么，你将`19`输入控制台，后面就可以输入信息了（对方输入`46`后进入解码模式）。例如这样：
```
[Input] Your message: Hello World!
[Send] GohepP8BOKrtj7IyJVhLRw==
```

你可以输入任何信息（包括中文），生成的密文是`base64`形式的一个字符串（就是`[Send]`后面的字符串，不过别想着去给它破解来看，你会得到一个扭曲的字符串），
此时你可以把密文**发给对面的朋友**。

现在我们以解密方的视角继续说明。对方收到你的信息时，他将收到的密文输入控制台，就像这样：
```
[Input] Your code: GohepP8BOKrtj7IyJVhLRw==
[Return] Hello World!
```
同时，说明一点：虽然你们可以就这样不停的传加密信息，但是重启程序之后（即重新输入`g`和`p`之后），你们必须将前面的操作重新做一遍。

## 关于这个程序

这个程序可以在平时用来装逼、在公屏里说悄悄话或者阻止他人查你的聊天记录。但是请不要和你的老板、家长、老师或者npy用这个开**过分**的玩笑。
在使用的同时请时刻记住要把握分寸。虽然别人无法破译你的信息，但是请勿用这个程序发布违法内容。

欢迎提出修改意见或者 Bug 。如果你喜欢这个程序，请给一颗星星支持，让更多人知道有这个聊天工具的存在。
