class URLShortener:
    id = 10000000000
    url2id = {}

    def url_shortener(self, url):
        if url in self.url2id:
            short_url = self.encode(self.url2id[url])

        else:
            self.url2id[url] = self.id
            short_url = self.encode(self.id)
            self.id += 1

        return "short_url.com/" + short_url

    def encode(self, id):
        chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(chars)
        remainders = []
        while id > 0:
            val = id % base
            remainders.append(chars[val])
            id //= base
        return ''.join(remainders[::-1])

short_url = URLShortener()
print(short_url.url_shortener("goooooooooooooogle.com"))
print(short_url.url_shortener("goooooooooooooogle.com"))
print(short_url.url_shortener("veryloooooooongurl.com"))
print(short_url.url_shortener("helllloooooooooooo.com"))
print(short_url.url_shortener("https://coding_interview.com/questions/183658/replacing-letters-with-number"))