from MatrixCollection import MatrixCollection as mc
import Util

class SHA512:
  def __init__(self):
    # Define constants
    self._k = getattr(mc, 'K')
    # Define initial hash value
    self._h = getattr(mc, 'H')
    
  def _prepare(self, plaintext):
    # Ubah plaintext ke dalam bentuk hex
    plaintext = Util.plainToBin(plaintext)
    # Tambah '1' bit
    self._plaintextLength = len(plaintext)
    plaintext += '1'
    # Tambah padding '0' bit sehingga panjang plaintext % 1024 = 896
    while(len(plaintext) % 1024 != 896):
      plaintext += '0'
    # tambahkan panjang plaintext
    plaintext += Util.decToBinary(self._plaintextLength, 128)
    # Bagi plaintext menjadi chunk 1024-bit
    chunks = [plaintext[i:i+1024] for i in range(0, len(plaintext), 1024)]
    return chunks

  def _processChunk(self, chunk):
    # Buat 16 block 64-bit dari chunk
    w = [chunk[i:i+64] for i in range(0, len(chunk), 64)]
    # Extend 16 block menjadi 80 block
    for i in range(16, 80):
      s1 = self._rotr(Util.binaryToDec(w[i-2]), 19) ^ self._rotr(Util.binaryToDec(w[i-2]), 61) ^ self._shr(Util.binaryToDec(w[i-2]), 6)
      s0 = self._rotr(Util.binaryToDec(w[i-15]), 1) ^ self._rotr(Util.binaryToDec(w[i-15]), 8) ^ self._shr(Util.binaryToDec(w[i-15]), 7)
      w.append(Util.decToBinary((s1 + Util.binaryToDec(w[i-7]) + s0 + Util.binaryToDec(w[i-16])) % pow(2, 64), 64))
    return w

  def _roundFunction(self, w):
    # Buat variabel untuk menyimpan nilai hash
    a, b, c, d, e, f, g, h = self._h
    # Proses hash
    for i in range(80):
      t1 = (Util.hexToDec(h) + self._sigma1(Util.hexToDec(e)) + self._ch(Util.hexToDec(e), Util.hexToDec(f), Util.hexToDec(g)) + Util.hexToDec(self._k[i]) + Util.binaryToDec(w[i])) % pow(2, 64)
      t2 = (self._sigma0(Util.hexToDec(a)) + self._maj(Util.hexToDec(a), Util.hexToDec(b), Util.hexToDec(c))) % pow(2, 64)
      h = g
      g = f
      f = e
      e = Util.decToHex((Util.hexToDec(d) + t1) % pow(2, 64))
      d = c
      c = b
      b = a
      a = Util.decToHex((t1 + t2) % pow(2, 64))
    # Update nilai hash
    self._h[0] = Util.decToHex((Util.hexToDec(a) + Util.hexToDec(self._h[0])) % pow(2, 64))
    self._h[1] = Util.decToHex((Util.hexToDec(b) + Util.hexToDec(self._h[1])) % pow(2, 64))
    self._h[2] = Util.decToHex((Util.hexToDec(c) + Util.hexToDec(self._h[2])) % pow(2, 64))
    self._h[3] = Util.decToHex((Util.hexToDec(d) + Util.hexToDec(self._h[3])) % pow(2, 64))
    self._h[4] = Util.decToHex((Util.hexToDec(e) + Util.hexToDec(self._h[4])) % pow(2, 64))
    self._h[5] = Util.decToHex((Util.hexToDec(f) + Util.hexToDec(self._h[5])) % pow(2, 64))
    self._h[6] = Util.decToHex((Util.hexToDec(g) + Util.hexToDec(self._h[6])) % pow(2, 64))
    self._h[7] = Util.decToHex((Util.hexToDec(h) + Util.hexToDec(self._h[7])) % pow(2, 64))

  def _digest(self):
    # Ubah nilai hash ke dalam bentuk hex
    digest = ''
    for i in range(len(self._h)):
      digest += self._h[i]
    return digest

  def hash(self, plaintext):
    # Proses hash
    chunks = self._prepare(plaintext)
    # print('Chunk: ', Util.binToHex(chunks[0]))
    for chunk in chunks:
      w = self._processChunk(chunk)
      self._roundFunction(w)
    # Hasil hash
    return self._digest()

  # fungsi ROTR
  def _rotr(self, x, n):
    # Rotasi sirkular kanan sebanyak n bits
    return (x >> n) | (x << (64 - n))

  # fungsi SHR
  def _shr(self, x, n):
    # Shift kanan sebanyak n bits
    return x >> n

  # fungsi Ch
  def _ch(self, e, f, g):
    return (e & f) ^ (~e & g)

  # fungsi Maj
  def _maj(self, a, b, c):
    return (a & b) ^ (a & c) ^ (b & c)

  # fungsi Sigma0
  def _sigma0(self, x):
    return self._rotr(x, 28) ^ self._rotr(x, 34) ^ self._rotr(x, 39)

  # fungsi Sigma1
  def _sigma1(self, x):
    return self._rotr(x, 14) ^ self._rotr(x, 18) ^ self._rotr(x, 41)
