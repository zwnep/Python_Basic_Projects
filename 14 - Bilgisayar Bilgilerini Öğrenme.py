
#   Bilgisayar bilgilerini öğrenme
#   Bu benim bilgisayarım için doğru bir şekilde çalıştı.
#   Ama sizin bilgisayarınızda farklılık gösterebilir veya çalışmayadabilir.

import os

b = os.uname()
print(b)
print("""
    İşletim sistemi : {} {}
    Bilgisayar adı  : {}
    Sürüm           : {}
    Sürüm tarihi    : {}
""".format(
    b.sysname, b.machine,
    b.nodename,
    b.release,
    b.version))

