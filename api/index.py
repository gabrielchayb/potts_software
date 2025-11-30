from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestão Pré-Natal Inteligente</title>
    
    <script src="https://cdn.tailwindcss.com"></script>
    
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <script src="https://unpkg.com/@phosphor-icons/web"></script>

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                    colors: {
                        medical: {
                            50: '#ecfdf5',
                            100: '#d1fae5',
                            500: '#10b981', // Verde Esmeralda Principal
                            600: '#059669',
                            900: '#064e3b',
                        }
                    }
                }
            }
        }
    </script>

    <style>
        /* Mesh Gradient Moderno */
        .mesh-bg {
            background-color: #ffffff;
            background-image: 
                radial-gradient(at 40% 20%, hsla(140,70%,90%,1) 0px, transparent 50%),
                radial-gradient(at 80% 0%, hsla(160,60%,92%,1) 0px, transparent 50%),
                radial-gradient(at 0% 50%, hsla(145,80%,94%,1) 0px, transparent 50%);
        }
        
        /* Transições suaves */
        .view-section {
            display: none;
            animation: fadeIn 0.4s ease-in-out;
        }
        
        .view-section.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 h-screen flex overflow-hidden font-sans">

    <aside class="w-64 bg-white border-r border-gray-200 flex flex-col justify-between z-10 shadow-sm">
        <div>
            <div class="h-16 flex items-center px-6 border-b border-gray-100">
                <i class="ph-fill ph-dna text-medical-600 text-2xl mr-2"></i>
                <span class="font-bold text-lg text-gray-800">Natal<span class="text-medical-600">AI</span></span>
            </div>

            <nav class="mt-6 px-4 space-y-2">
                <a href="#" onclick="showView('dashboard')" class="nav-item flex items-center px-4 py-3 text-sm font-medium rounded-lg bg-medical-50 text-medical-900 group transition-colors">
                    <i class="ph ph-squares-four text-xl mr-3"></i>
                    Dashboard
                </a>
                <a href="#" onclick="showView('paciente')" class="nav-item flex items-center px-4 py-3 text-sm font-medium rounded-lg text-gray-600 hover:bg-gray-50 hover:text-gray-900 group transition-colors">
                    <i class="ph ph-user text-xl mr-3"></i>
                    Histórico Clínico
                </a>
                <a href="#" onclick="showView('analise')" class="nav-item flex items-center px-4 py-3 text-sm font-medium rounded-lg text-gray-600 hover:bg-gray-50 hover:text-gray-900 group transition-colors">
                    <i class="ph ph-brain text-xl mr-3"></i>
                    Análise IA
                    <span class="ml-auto bg-medical-100 text-medical-900 py-0.5 px-2 rounded-full text-xs font-semibold">Novo</span>
                </a>
                <a href="#" onclick="showView('decisao')" class="nav-item flex items-center px-4 py-3 text-sm font-medium rounded-lg text-gray-600 hover:bg-gray-50 hover:text-gray-900 group transition-colors">
                    <i class="ph ph-stethoscope text-xl mr-3"></i>
                    Apoio à Decisão
                </a>
            </nav>
        </div>

        <div class="p-4 border-t border-gray-100">
            <div class="flex items-center gap-3">
                <img src="https://ui-avatars.com/api/?name=Dr+Silva&background=059669&color=fff" class="w-10 h-10 rounded-full">
                <div>
                    <p class="text-sm font-medium text-gray-700">Dra. Eliane Espindola</p>
                    <p class="text-xs text-gray-500">Obstetra</p>
                </div>
            </div>
        </div>
    </aside>

    <main class="flex-1 overflow-y-auto mesh-bg p-8">
        
        <header class="flex justify-between items-center mb-8">
            <div>
                <h1 id="page-title" class="text-2xl font-bold text-gray-900">Visão Geral</h1>
                <p class="text-gray-500 text-sm mt-1">A melhor tecnologia para cuidar das nossas buchudinhas!</p>
            </div>
            <div class="flex gap-3">
                <button class="p-2 bg-white rounded-full shadow-sm text-gray-500 hover:text-medical-600 transition"><i class="ph ph-bell text-xl"></i></button>
                <button class="bg-medical-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-medical-900 transition flex items-center gap-2 shadow-lg shadow-medical-500/30">
                    <i class="ph ph-plus"></i> Novo Exame
                </button>
            </div>
        </header>

        <div id="dashboard" class="view-section active space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
                <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
                    <div class="flex justify-between items-start">
                        <div>
                            <p class="text-xs font-medium text-gray-500 uppercase">Pacientes Ativas</p>
                            <h3 class="text-2xl font-bold text-gray-900 mt-2">142</h3>
                        </div>
                        <span class="p-2 bg-blue-50 text-blue-600 rounded-lg"><i class="ph ph-users"></i></span>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
                    <div class="flex justify-between items-start">
                        <div>
                            <p class="text-xs font-medium text-gray-500 uppercase">Exames Pendentes</p>
                            <h3 class="text-2xl font-bold text-gray-900 mt-2">12</h3>
                        </div>
                        <span class="p-2 bg-yellow-50 text-yellow-600 rounded-lg"><i class="ph ph-clock"></i></span>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
                    <div class="flex justify-between items-start">
                        <div>
                            <p class="text-xs font-medium text-gray-500 uppercase">Alertas de Risco</p>
                            <h3 class="text-2xl font-bold text-red-600 mt-2">3</h3>
                        </div>
                        <span class="p-2 bg-red-50 text-red-600 rounded-lg"><i class="ph ph-warning"></i></span>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
                    <div class="flex justify-between items-start">
                        <div>
                            <p class="text-xs font-medium text-gray-500 uppercase">Precisão da IA</p>
                            <h3 class="text-2xl font-bold text-medical-600 mt-2">98.4%</h3>
                        </div>
                        <span class="p-2 bg-medical-50 text-medical-600 rounded-lg"><i class="ph ph-chart-line-up"></i></span>
                    </div>
                </div>
            </div>

            <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                <div class="px-6 py-4 border-b border-gray-100">
                    <h3 class="font-semibold text-gray-800">Atividades Recentes</h3>
                </div>
                <table class="w-full text-sm text-left">
                    <thead class="text-xs text-gray-500 uppercase bg-gray-50">
                        <tr>
                            <th class="px-6 py-3">Paciente</th>
                            <th class="px-6 py-3">Exame</th>
                            <th class="px-6 py-3">Status IA</th>
                            <th class="px-6 py-3">Ação</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b hover:bg-gray-50 transition">
                            <td class="px-6 py-4 font-medium text-gray-900">Mariana Costa (24ª sem)</td>
                            <td class="px-6 py-4">Ultrassom Morfológico</td>
                            <td class="px-6 py-4"><span class="bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full">Normal</span></td>
                            <td class="px-6 py-4"><a href="#" onclick="showView('paciente')" class="text-medical-600 hover:underline">Ver</a></td>
                        </tr>
                        <tr class="border-b hover:bg-gray-50 transition">
                            <td class="px-6 py-4 font-medium text-gray-900">Julia Santos (12ª sem)</td>
                            <td class="px-6 py-4">Hemograma Completo</td>
                            <td class="px-6 py-4"><span class="bg-yellow-100 text-yellow-800 text-xs px-2 py-1 rounded-full flex items-center gap-1 w-fit"><i class="ph-fill ph-warning"></i> Atenção</span></td>
                            <td class="px-6 py-4"><a href="#" onclick="showView('analise')" class="text-medical-600 hover:underline">Analisar</a></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div id="paciente" class="view-section space-y-6">
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 flex items-center justify-between">
                <div class="flex items-center gap-4">
                    <div class="w-16 h-16 rounded-full bg-medical-100 flex items-center justify-center text-medical-700 text-xl font-bold">JS</div>
                    <div>
                        <h2 class="text-xl font-bold text-gray-900">Julia Santos</h2>
                        <p class="text-gray-500">32 anos • G1P0A0 • 12ª Semana + 4 dias</p>
                    </div>
                </div>
                <div class="flex gap-2">
                    <span class="px-3 py-1 border border-gray-200 rounded-lg text-sm font-medium">Tipo Sanguíneo: A+</span>
                    <span class="px-3 py-1 border border-red-200 bg-red-50 text-red-700 rounded-lg text-sm font-medium">Alergia: Penicilina</span>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="lg:col-span-2 space-y-6">
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
                        <h3 class="font-semibold text-gray-800 mb-4 flex items-center gap-2">
                            <i class="ph ph-files text-medical-600"></i> Repositório de Exames
                        </h3>
                        
                        <div class="flex border-b border-gray-200 mb-4">
                            <button class="px-4 py-2 border-b-2 border-medical-500 text-medical-700 font-medium">Laboratoriais</button>
                            <button class="px-4 py-2 text-gray-500 hover:text-gray-700">Imagem</button>
                            <button class="px-4 py-2 text-gray-500 hover:text-gray-700">Histórico Clínico</button>
                        </div>

                        <div class="space-y-4">
                            <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg border border-gray-100">
                                <div class="flex items-center gap-3">
                                    <div class="bg-white p-2 rounded border border-gray-200">
                                        <i class="ph ph-drop text-red-500 text-xl"></i>
                                    </div>
                                    <div>
                                        <h4 class="font-medium text-gray-900">Hemograma e Glicemia</h4>
                                        <p class="text-xs text-gray-500">Realizado em 29/11/2025 • Lab. Central</p>
                                    </div>
                                </div>
                                <button onclick="showView('analise')" class="text-sm text-medical-600 font-medium border border-medical-200 px-3 py-1 rounded hover:bg-medical-50">Ver Análise IA</button>
                            </div>
                            
                            <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg border border-gray-100">
                                <div class="flex items-center gap-3">
                                    <div class="bg-white p-2 rounded border border-gray-200">
                                        <i class="ph ph-image text-blue-500 text-xl"></i>
                                    </div>
                                    <div>
                                        <h4 class="font-medium text-gray-900">USG Transvaginal</h4>
                                        <p class="text-xs text-gray-500">Realizado em 15/10/2025 • Clínica Imagem</p>
                                    </div>
                                </div>
                                <button class="text-sm text-gray-600 font-medium border border-gray-200 px-3 py-1 rounded hover:bg-gray-100">Abrir Viewer</button>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="space-y-6">
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
                        <h3 class="font-semibold text-gray-800 mb-4">Sinais Vitais (Última Consulta)</h3>
                        <div class="space-y-4">
                            <div>
                                <div class="flex justify-between text-sm mb-1">
                                    <span class="text-gray-500">Pressão Arterial</span>
                                    <span class="font-bold text-gray-900">110/70 mmHg</span>
                                </div>
                                <div class="w-full bg-gray-100 rounded-full h-2">
                                    <div class="bg-medical-500 h-2 rounded-full" style="width: 40%"></div>
                                </div>
                            </div>
                            <div>
                                <div class="flex justify-between text-sm mb-1">
                                    <span class="text-gray-500">Peso</span>
                                    <span class="font-bold text-gray-900">62.5 kg</span>
                                </div>
                                <div class="w-full bg-gray-100 rounded-full h-2">
                                    <div class="bg-blue-500 h-2 rounded-full" style="width: 60%"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div id="analise" class="view-section space-y-6">
            <div class="flex gap-6 h-[600px]">
                <div class="w-1/2 bg-white rounded-xl shadow-sm border border-gray-100 p-4 flex flex-col">
                    <h3 class="font-semibold text-gray-800 mb-4 border-b pb-2">Resultado Laboratorial (OCR)</h3>
                    <div class="flex-1 bg-gray-50 p-4 font-mono text-xs overflow-y-auto text-gray-600 leading-relaxed border border-gray-200 rounded">
                        <p>PACIENTE: JULIA SANTOS</p>
                        <p>DATA: 29/11/2025</p>
                        <br>
                        <p>ERITROGRAMA:...............4.20 milhoes/mm3</p>
                        <p>HEMOGLOBINA:..............10.9 g/dL (Ref: 12.0 a 15.5)</p>
                        <p>HEMATOCRITO:..............34.0 %</p>
                        <br>
                        <p>FERRITINA:................12 ng/mL (Ref: 15 a 150)</p>
                        <p>GLICEMIA JEJUM:...........82 mg/dL</p>
                        <p>TSH:......................2.5 uUI/mL</p>
                        <br>
                        <p>OBS: Amostra confirmada.</p>
                    </div>
                </div>

                <div class="w-1/2 flex flex-col gap-4">
                    <div class="bg-gradient-to-br from-medical-900 to-medical-600 text-white rounded-xl shadow-lg p-6 relative overflow-hidden">
                        <div class="absolute top-0 right-0 p-4 opacity-10">
                            <i class="ph-fill ph-brain text-9xl"></i>
                        </div>
                        <div class="relative z-10">
                            <h3 class="text-lg font-bold flex items-center gap-2"><i class="ph ph-sparkle"></i> Análise Preditiva</h3>
                            <p class="text-medical-100 text-sm mt-1">Processado por Modelo Med-LLM v4</p>
                            
                            <div class="mt-6 space-y-3">
                                <div class="bg-white/10 backdrop-blur-md rounded-lg p-3 border border-white/20">
                                    <div class="flex items-center gap-2 text-yellow-300 font-bold mb-1">
                                        <i class="ph-fill ph-warning-circle"></i> Anemia Leve Detectada
                                    </div>
                                    <p class="text-sm text-gray-100">Hemoglobina (10.9) e Ferritina (12) abaixo dos valores de referência para o segundo trimestre.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 flex-1">
                        <h3 class="font-semibold text-gray-800 mb-4">Interpretação e Contexto</h3>
                        <p class="text-gray-600 text-sm mb-4">A IA cruzou os dados laboratoriais com o histórico clínico da paciente (G1P0A0). Não há histórico de talassemia.</p>
                        
                        <h4 class="text-sm font-bold text-gray-900 mb-2">Sugestão de Conduta:</h4>
                        <ul class="list-disc list-inside text-sm text-gray-600 space-y-1">
                            <li>Investigar deficiência de ferro (anemia ferropriva).</li>
                            <li>Considerar suplementação oral de Sulfato Ferroso.</li>
                            <li>Repetir exame em 30 dias.</li>
                        </ul>
                        
                        <div class="mt-6 pt-4 border-t border-gray-100 text-center">
                            <button onclick="showView('decisao')" class="bg-medical-50 text-medical-700 font-medium px-4 py-2 rounded-lg hover:bg-medical-100 w-full transition">Ir para Apoio à Decisão</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div id="decisao" class="view-section space-y-6">
            <div class="bg-yellow-50 border border-yellow-200 rounded-xl p-4 flex items-start gap-3">
                <i class="ph-fill ph-lightbulb text-yellow-600 text-xl mt-1"></i>
                <div>
                    <h3 class="font-bold text-yellow-800">Protocolo Sugerido: Anemia na Gestação</h3>
                    <p class="text-sm text-yellow-700 mt-1">Baseado nas diretrizes da FEBRASGO e nos resultados laboratoriais recentes.</p>
                </div>
            </div>

            <div class="grid grid-cols-2 gap-6">
                <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 hover:shadow-md transition cursor-pointer group">
                    <div class="flex justify-between items-start mb-4">
                        <div class="p-3 bg-medical-50 rounded-lg text-medical-600 group-hover:bg-medical-600 group-hover:text-white transition">
                            <i class="ph ph-pill text-2xl"></i>
                        </div>
                        <input type="checkbox" class="w-5 h-5 text-medical-600 rounded border-gray-300 focus:ring-medical-500">
                    </div>
                    <h3 class="font-bold text-gray-900">Gerar Prescrição</h3>
                    <p class="text-sm text-gray-500 mt-2">Sulfato Ferroso 40mg - 1 cp via oral antes do almoço.</p>
                </div>

                <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 hover:shadow-md transition cursor-pointer group">
                    <div class="flex justify-between items-start mb-4">
                        <div class="p-3 bg-blue-50 rounded-lg text-blue-600 group-hover:bg-blue-600 group-hover:text-white transition">
                            <i class="ph ph-file-text text-2xl"></i>
                        </div>
                        <input type="checkbox" class="w-5 h-5 text-blue-600 rounded border-gray-300 focus:ring-blue-500">
                    </div>
                    <h3 class="font-bold text-gray-900">Solicitar Retorno</h3>
                    <p class="text-sm text-gray-500 mt-2">Hemograma de controle em 4 semanas.</p>
                </div>
                
                <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 hover:shadow-md transition cursor-pointer group">
                    <div class="flex justify-between items-start mb-4">
                        <div class="p-3 bg-purple-50 rounded-lg text-purple-600 group-hover:bg-purple-600 group-hover:text-white transition">
                            <i class="ph ph-chats text-2xl"></i>
                        </div>
                        <input type="checkbox" class="w-5 h-5 text-purple-600 rounded border-gray-300 focus:ring-purple-500">
                    </div>
                    <h3 class="font-bold text-gray-900">Enviar Orientação Nutricional</h3>
                    <p class="text-sm text-gray-500 mt-2">Enviar PDF via WhatsApp com dieta rica em ferro.</p>
                </div>
            </div>
            
            <div class="fixed bottom-8 right-8">
                <button class="bg-gray-900 text-white px-6 py-3 rounded-full shadow-xl font-medium flex items-center gap-2 hover:scale-105 transition">
                    <i class="ph ph-check"></i> Confirmar Conduta
                </button>
            </div>
        </div>

    </main>

    <script>
        function showView(viewId) {
            // Ocultar todas as views
            document.querySelectorAll('.view-section').forEach(el => {
                el.classList.remove('active');
            });
            
            // Remover estado ativo do menu
            document.querySelectorAll('.nav-item').forEach(el => {
                el.classList.remove('bg-medical-50', 'text-medical-900');
                el.classList.add('text-gray-600');
            });

            // Mostrar view selecionada
            const target = document.getElementById(viewId);
            if(target) {
                target.classList.add('active');
            }

            // Atualizar título da página (Simples)
            const titles = {
                'dashboard': 'Visão Geral',
                'paciente': 'Histórico Clínico',
                'analise': 'Análise Inteligente',
                'decisao': 'Apoio à Decisão Médica'
            };
            document.getElementById('page-title').innerText = titles[viewId];
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

# Necessário para a Vercel
if __name__ == '__main__':
    app.run()