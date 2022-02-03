#import matplotlib.pyplot as plt

#plt.plot([1120, 3360, 7839, 16146, 26387, 43510, 63529], [2, 4, 8, 16, 32, 64, 100], 'ro')
#plt.axis([0, 6, 0, 20])
#plt.show()

import matplotlib.pyplot as plt
plt.tight_layout()

# 512 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [1120, 3360, 7838, 15479, 18034, 16442, 16168], 'go-', label='RX Packet Sum (512 bytes)', linewidth=3, color='#34c3b9')

# 1024 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [1120, 3360, 7839, 13003, 11350, 13109, 12637], 'go-', label='RX Packet Sum (1024 bytes)', linewidth=3, color='#e99579')

# 1500 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [1120, 3360, 7834, 6939, 6958, 8523, 7032], 'go-', label='RX Packet Sum (1500 bytes)', linewidth=3, color='#0066ff')

plt.ylabel('Soma de Pacotes Recebidos (Unidade)', fontsize='large',)
plt.xlabel('Número de nós da rede (Unidade)', fontsize='large')
plt.title("Soma dos Pacotes Recebidos na rede Halteres \n com tamanho de pacotes 512 bytes, 1024 bytes e 1500 bytes", fontsize=20	, fontweight='bold')
plt.legend()
plt.show()
