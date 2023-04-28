import js2py

js_content = """
var g = {
            Decrypt: function(e) {
                var t = p.a.enc.Utf8.parse(f)
                  , i = p.a.enc.Utf8.parse(v)
                  , s = p.a.enc.Hex.parse(e)
                  , a = p.a.enc.Base64.stringify(s);
                return p.a.AES.decrypt(a, t, {
                    iv: i,
                    mode: p.a.mode.CBC,
                    padding: p.a.pad.Pkcs7
                }).toString(p.a.enc.Utf8).toString()
            },
            Encrypt: function(e) {
                var t = p.a.enc.Utf8.parse(f)
                  , i = p.a.enc.Utf8.parse(v)
                  , s = p.a.enc.Utf8.parse(e);
                return p.a.AES.encrypt(s, t, {
                    iv: i,
                    mode: p.a.mode.CBC,
                    padding: p.a.pad.Pkcs7
                }).ciphertext.toString()
            }
        }
"""

context = js2py.EvalJs()
context.execute(js_content)
result = context.g.Encrypt("1q2w3e4r@")
print(result)
