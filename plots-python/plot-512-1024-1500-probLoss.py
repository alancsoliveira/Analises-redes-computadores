import matplotlib.pyplot as plt
plt.tight_layout()

# 512 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [0, 0, 0, 4, 31, 62, 74], 'go-', label='Packets Lost Ratio (512 bytes)', linewidth=3, color='#34c3b9')

# 1024 bytes

plt.plot([2, 4, 8, 16, 32, 64, 100], [0, 0, 0, 14, 52, 68, 79], 'go-', label='Packets Lost Ratio (1024 bytes)', linewidth=3, color='#e99579')

# 1500 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [0, 0, 0, 45, 68, 78, 88], 'go-', label='Packets Lost Ratio (1500 bytes)', linewidth=3, color='#0066ff')

plt.ylabel('Taxa de pacotes perdidos (%)', fontsize='large',)
plt.xlabel('Número de nós da rede (Unidade)', fontsize='large')
plt.title("Taxa de pacotes perdidos na rede Halteres \n com tamanho de pacotes 512 bytes, 1024 bytes e 1500 bytes", fontsize=20, fontweight='bold')
plt.legend()
plt.show()
