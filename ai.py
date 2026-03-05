import google.generativeai as genai

# Masukkan API Key kamu di sini
genai.configure(api_key="papi.b33e4be8-d552-4451-b7fe-977c36033283.xgcCMTmFuU_DaTnG30f0zbIcJbmWmff9")

# Pilih model Gemini
model = genai.GenerativeModel("gemini-1.5-flash")

# Kirim prompt ke Gemini
response = model.generate_content("Jelaskan apa itu machine learning secara singkat")

# Cetak hasil respon
print(response.text)