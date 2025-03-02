import speedtest

st = speedtest.Speedtest()

# Obtém os melhores servidores
st.get_best_server()

# Medindo a velocidade de download e upload
download_speed = st.download() / 1_000_000  # Convertendo de bits para megabits
upload_speed = st.upload() / 1_000_000  # Convertendo de bits para megabits

# Medindo o ping
ping = st.results.ping

print(f"Download speed: {download_speed:.2f} Mbps")
print(f"Upload speed: {upload_speed:.2f} Mbps")
print(f"Ping: {ping} ms")
