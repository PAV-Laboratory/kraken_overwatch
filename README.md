# Kraken Overwatch
A fun script of mine to watch changes in cryptocurrency :grinning:

**WARNING**: the script is raw, has bugs etc.

## Description
This is a modified **Kraken API Example** script.

You can run it with:

``` .\kraken.py <cryptoname-fiat> <unixtime now> <threshold for alarm> ```

For example:

``` .\kraken.py XXRPZUSD 1612658747 0.7 ```

![Image of Uploaded fruits](https://github.com/brtemik/kraken_overwatch/blob/main/kraken_screenshot.JPG)

The names of crypto labels that I found to work:
* XETHZUSD: Etherium to USD
* GRTUSD: Graph to USD
* XLTCZUSD: Litecoin to USD
* XXRPZUSD: Ripple to USD

What it does: It requests the price of a coin from a market (Kraken) and remembers it (first four digits). If it changes - you get the info in CLI and also robo-voice says the price. When the price reaches the treshold the Erebor horn sounds.
