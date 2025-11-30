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
                            500: '#10b981',
                            600: '#059669',
                            900: '#064e3b',
                        }
                    }
                }
            }
        }
    </script>

    <style>
        .mesh-bg {
            background-color: #ffffff;
            background-image: 
                radial-gradient(at 40% 20%, hsla(140,70%,90%,1) 0px, transparent 50%),
                radial-gradient(at 80% 0%, hsla(160,60%,92%,1) 0px, transparent 50%),
                radial-gradient(at 0% 50%, hsla(145,80%,94%,1) 0px, transparent 50%);
        }
        
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

        /* Animação do Popover de Notificação */
        #notification-panel {
            transform-origin: top right;
            transition: all 0.2s ease-out;
        }
        
        .hidden-popover {
            opacity: 0;
            transform: scale(0.95);
            pointer-events: none;
        }
        
        .visible-popover {
            opacity: 1;
            transform: scale(1);
            pointer-events: auto;
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

    <main class="flex-1 overflow-y-auto mesh-bg p-8 relative">
        
        <header class="flex justify-between items-center mb-8 relative">
            <div>
                <h1 id="page-title" class="text-2xl font-bold text-gray-900">Visão Geral</h1>
                <p class="text-gray-500 text-sm mt-1">A melhor tecnologia para cuidar das nossas buchudinhas!</p>
            </div>
            <div class="flex gap-3 relative">
                <button onclick="toggleNotifications()" class="p-2 bg-white rounded-full shadow-sm text-gray-500 hover:text-medical-600 transition relative">
                    <i class="ph ph-bell text-xl"></i>
                    <span class="absolute top-0 right-0 h-3 w-3 bg-red-500 rounded-full border-2 border-white"></span>
                </button>

                <div id="notification-panel" class="hidden-popover absolute top-12 right-0 w-80 bg-white rounded-xl shadow-xl border border-gray-100 z-50">
                    <div class="p-4 border-b border-gray-100 flex justify-between items-center">
                        <h3 class="font-bold text-sm text-gray-800">Notificações</h3>
                        <span class="text-xs text-medical-600 font-medium cursor-pointer">Marcar lidas</span>
                    </div>
                    <div class="max-h-64 overflow-y-auto">
                        <div class="p-4 border-b border-gray-50 hover:bg-gray-50 cursor-pointer">
                            <div class="flex gap-3">
                                <div class="mt-1 h-2 w-2 rounded-full bg-red-500 flex-shrink-0"></div>
                                <div>
                                    <p class="text-sm font-medium text-gray-800">Risco Elevado: Ana Clara</p>
                                    <p class="text-xs text-gray-500 mt-1">Pressão arterial acima do normal detectada no último registro.</p>
                                    <p class="text-xs text-gray-400 mt-2">Há 10 min</p>
                                </div>
                            </div>
                        </div>
                        <div class="p-4 border-b border-gray-50 hover:bg-gray-50 cursor-pointer">
                            <div class="flex gap-3">
                                <div class="mt-1 h-2 w-2 rounded-full bg-blue-500 flex-shrink-0"></div>
                                <div>
                                    <p class="text-sm font-medium text-gray-800">Novo Exame Disponível</p>
                                    <p class="text-xs text-gray-500 mt-1">O laboratório enviou os resultados de Julia Santos.</p>
                                    <p class="text-xs text-gray-400 mt-2">Há 1 hora</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="p-3 text-center border-t border-gray-100">
                        <a href="#" class="text-xs font-medium text-gray-600 hover:text-medical-600">Ver todas</a>
                    </div>
                </div>

                <button onclick="showView('novo-exame')" class="bg-medical-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-medical-900 transition flex items-center gap-2 shadow-lg shadow-medical-500/30">
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
                            <td class="px-6 py-4"><a href="#" onclick="showView('mariana-profile')" class="text-medical-600 hover:underline font-medium">Ver</a></td>
                        </tr>
                        <tr class="border-b hover:bg-gray-50 transition">
                            <td class="px-6 py-4 font-medium text-gray-900">Julia Santos (12ª sem)</td>
                            <td class="px-6 py-4">Hemograma Completo</td>
                            <td class="px-6 py-4"><span class="bg-yellow-100 text-yellow-800 text-xs px-2 py-1 rounded-full flex items-center gap-1 w-fit"><i class="ph-fill ph-warning"></i> Atenção</span></td>
                            <td class="px-6 py-4"><a href="#" onclick="showView('analise')" class="text-medical-600 hover:underline font-medium">Analisar</a></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div id="novo-exame" class="view-section space-y-6">
            <div class="max-w-3xl mx-auto">
                <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-8">
                    <h2 class="text-xl font-bold text-gray-900 mb-6">Importar Novos Exames</h2>
                    
                    <div class="border-2 border-dashed border-medical-200 rounded-xl bg-medical-50 p-12 text-center cursor-pointer hover:bg-medical-100 transition group">
                        <div class="w-16 h-16 bg-white text-medical-500 rounded-full flex items-center justify-center mx-auto mb-4 shadow-sm group-hover:scale-110 transition">
                            <i class="ph ph-cloud-arrow-up text-3xl"></i>
                        </div>
                        <h3 class="text-lg font-medium text-gray-900">Arraste e solte seus PDFs aqui</h3>
                        <p class="text-gray-500 mt-2 mb-6">Ou clique para selecionar do computador</p>
                        
                        <button class="bg-white border border-gray-200 text-gray-700 px-4 py-2 rounded-lg text-sm font-medium hover:bg-gray-50">
                            Selecionar Arquivos
                        </button>
                    </div>

                    <div class="mt-6">
                        <div class="flex justify-between items-center text-xs text-gray-500 mb-2">
                            <span>Limite de Upload</span>
                            <span>Até 10MB Total</span>
                        </div>
                        <div class="w-full bg-gray-100 rounded-full h-1.5">
                            <div class="bg-gray-300 h-1.5 rounded-full" style="width: 0%"></div>
                        </div>
                        <p class="text-xs text-gray-400 mt-2 flex items-center gap-1">
                            <i class="ph ph-info"></i> Suporta múltiplos arquivos PDF simultaneamente.
                        </p>
                    </div>

                    <div class="mt-8 flex justify-end gap-3">
                        <button onclick="showView('dashboard')" class="px-4 py-2 text-gray-600 hover:bg-gray-100 rounded-lg text-sm font-medium transition">Cancelar</button>
                        <button onclick="alert('Sistema demo: Upload simulado com sucesso!')" class="px-6 py-2 bg-medical-600 text-white rounded-lg text-sm font-medium hover:bg-medical-900 shadow-lg shadow-medical-500/30 transition">
                            Processar Exames com IA
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <div id="mariana-profile" class="view-section space-y-6">
            <div class="flex items-center gap-2 mb-4">
                <button onclick="showView('dashboard')" class="text-gray-400 hover:text-gray-700"><i class="ph ph-arrow-left text-xl"></i></button>
                <span class="text-sm text-gray-500">Voltar para lista</span>
            </div>

            <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 flex items-center justify-between border-l-4 border-l-purple-500">
                <div class="flex items-center gap-4">
                    <div class="w-16 h-16 rounded-full bg-purple-100 flex items-center justify-center text-purple-700 text-xl font-bold">MC</div>
                    <div>
                        <h2 class="text-xl font-bold text-gray-900">Mariana Costa</h2>
                        <p class="text-gray-500">28 anos • G2P1A0 • <span class="text-purple-600 font-semibold">24ª Semana</span></p>
                    </div>
                </div>
                <div class="flex gap-2">
                    <span class="px-3 py-1 border border-gray-200 rounded-lg text-sm font-medium">Tipo Sanguíneo: O-</span>
                    <span class="px-3 py-1 bg-green-50 text-green-700 rounded-lg text-sm font-medium border border-green-200">Sem Alergias</span>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="lg:col-span-2 space-y-6">
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
                        <h3 class="font-semibold text-gray-800 mb-4 flex items-center gap-2">
                            <i class="ph ph-files text-purple-600"></i> Últimos Exames (2º Trimestre)
                        </h3>
                        
                        <div class="space-y-4">
                            <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg border border-gray-100">
                                <div class="flex items-center gap-3">
                                    <div class="bg-white p-2 rounded border border-gray-200">
                                        <i class="ph ph-baby text-purple-500 text-xl"></i>
                                    </div>
                                    <div>
                                        <h4 class="font-medium text-gray-900">Ultrassom Morfológico</h4>
                                        <p class="text-xs text-gray-500">Realizado hoje • Clínica Materna</p>
                                    </div>
                                </div>
                                <div class="flex gap-2">
                                    <span class="bg-green-100 text-green-800 text-xs font-bold px-2 py-1 rounded">Normal</span>
                                    <button class="text-sm text-gray-600 font-medium border border-gray-200 px-3 py-1 rounded hover:bg-gray-100">Ver Laudo</button>
                                </div>
                            </div>

                            <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg border border-gray-100 opacity-75">
                                <div class="flex items-center gap-3">
                                    <div class="bg-white p-2 rounded border border-gray-200">
                                        <i class="ph ph-drop text-red-500 text-xl"></i>
                                    </div>
                                    <div>
                                        <h4 class="font-medium text-gray-900">TOTG (Teste de Tolerância a Glicose)</h4>
                                        <p class="text-xs text-gray-500">Realizado há 1 semana</p>
                                    </div>
                                </div>
                                <span class="bg-green-100 text-green-800 text-xs font-bold px-2 py-1 rounded">Normal</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="space-y-6">
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
                        <h3 class="font-semibold text-gray-800 mb-4">Acompanhamento de Peso</h3>
                        <div class="space-y-4">
                            <div>
                                <div class="flex justify-between text-sm mb-1">
                                    <span class="text-gray-500">Ganho Total</span>
                                    <span class="font-bold text-gray-900">+6.5 kg</span>
                                </div>
                                <div class="w-full bg-gray-100 rounded-full h-2">
                                    <div class="bg-purple-500 h-2 rounded-full" style="width: 55%"></div>
                                </div>
                                <p class="text-xs text-gray-400 mt-1">Dentro do esperado para IMC inicial.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div id="paciente" class="view-section space-y-6">
            <div class="flex items-center gap-2 mb-4">
                <button onclick="showView('dashboard')" class="text-gray-400 hover:text-gray-700"><i class="ph ph-arrow-left text-xl"></i></button>
                <span class="text-sm text-gray-500">Voltar para lista</span>
            </div>
            
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
                        </div>
                    </div>
                </div>
                 <div class="space-y-6">
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
                        <h3 class="font-semibold text-gray-800 mb-4">Sinais Vitais</h3>
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
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div id="analise" class="view-section space-y-6">
             <div class="flex items-center gap-2 mb-4">
                <button onclick="showView('dashboard')" class="text-gray-400 hover:text-gray-700"><i class="ph ph-arrow-left text-xl"></i></button>
                <span class="text-sm text-gray-500">Voltar</span>
            </div>
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
                </div>
            </div>
            <div class="grid grid-cols-2 gap-6">
                <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 hover:shadow-md transition cursor-pointer group">
                    <h3 class="font-bold text-gray-900">Gerar Prescrição</h3>
                    <p class="text-sm text-gray-500 mt-2">Sulfato Ferroso 40mg.</p>
                </div>
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
            
            // Fechar notificações se mudar de tela
            const notifPanel = document.getElementById('notification-panel');
            notifPanel.classList.remove('visible-popover');
            notifPanel.classList.add('hidden-popover');

            // Atualizar título da página
            const titles = {
                'dashboard': 'Visão Geral',
                'paciente': 'Histórico Clínico: Julia Santos',
                'mariana-profile': 'Histórico Clínico: Mariana Costa',
                'novo-exame': 'Importar Exames',
                'analise': 'Análise Inteligente',
                'decisao': 'Apoio à Decisão Médica'
            };
            document.getElementById('page-title').innerText = titles[viewId] || 'NatalAI';
        }

        function toggleNotifications() {
            const panel = document.getElementById('notification-panel');
            if (panel.classList.contains('hidden-popover')) {
                panel.classList.remove('hidden-popover');
                panel.classList.add('visible-popover');
            } else {
                panel.classList.remove('visible-popover');
                panel.classList.add('hidden-popover');
            }
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