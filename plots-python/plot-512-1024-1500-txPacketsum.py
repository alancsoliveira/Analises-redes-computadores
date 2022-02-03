#import matplotlib.pyplot as plt

#plt.plot([1120, 3360, 7839, 16146, 26387, 43510, 63529], [2, 4, 8, 16, 32, 64, 100], 'ro')
#plt.axis([0, 6, 0, 20])
#plt.show()

import matplotlib.pyplot as plt
plt.tight_layout()

# 512 byte
plt.plot([2, 4, 8, 16, 32, 64, 100], [1120, 3360, 7839, 16146, 26387, 43510, 63529], 'go-', label='TX Packet Sum (512 bytes)', linewidth=3, color='#34c3b9')

# 1024 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [1120, 3360, 7840, 15125, 24093, 42249, 61963], 'go-', label='TX Packet Sum (1024 bytes)', linewidth=3, color='#e99579')

# 1500 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [1120, 3360, 7837, 12627, 21808, 40084, 59573], 'go-', label='TX Packet Sum (1500 bytes)', linewidth=3, color='#0066ff')

plt.ylabel('Soma de Pacotes Trasmitidos (Unidade)', fontsize='large',)
plt.xlabel('Número de nós da rede (Unidade)', fontsize='large')
plt.title("Soma dos Pacotes Transmitidos na rede Halteres \n com tamanho de pacotes 512 bytes, 1024 bytes e 1500 bytes", fontsize=20	, fontweight='bold')
plt.legend()
plt.show()
