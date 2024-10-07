function Encrypt(e) {
    var t = p.a.enc.Utf8.parse(f)
        , i = p.a.enc.Utf8.parse(v)
        , s = p.a.enc.Utf8.parse(e);
    return p.a.AES.encrypt(s, t, {
        iv: i,
        mode: p.a.mode.CBC,
        padding: p.a.pad.Pkcs7
    }).ciphertext.toString()
}