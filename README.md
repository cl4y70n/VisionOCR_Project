# **VisionOCR — Sistema de Leitura Automática de Documentos**

## **Descrição do Projeto**

O **VisionOCR** é um sistema inteligente para **extração e interpretação automática de informações de documentos digitais ou escaneados**, como:

* RG, CNH
* Notas fiscais
* Contratos ou formulários

Ele combina **Computer Vision (OCR)** com **NLP** para transformar imagens de documentos em dados estruturados (JSON), permitindo automação e integração com sistemas corporativos.

Principais técnicas:

* **OCR**: Tesseract OCR ou PaddleOCR para extração de texto.
* **NLP**: Transformers (BERT, RoBERTa) para classificação e extração de campos relevantes (nome, data, valor, CPF, etc.).
* **Pipeline completo**: Upload → OCR → Processamento → Classificação → Exportação JSON.
* **Dashboard/Interface**: Para upload e visualização interativa dos resultados.

---

## **Arquitetura do Projeto**

```
VisionOCR_Project/
│
├─ data/
│  ├─ raw/                   # Imagens originais dos documentos
│  ├─ processed/             # Imagens pré-processadas (binárias, redimensionadas)
│  └─ ocr_output/            # Textos extraídos via OCR
│
├─ src/
│  ├─ data_loader/           # Carregamento e manipulação de imagens
│  │  └─ load_images.py
│  ├─ preprocessing/         # Limpeza e pré-processamento das imagens
│  │  └─ image_preprocessing.py
│  ├─ ocr/                   # Pipeline OCR
│  │  └─ extract_text.py
│  ├─ nlp/                   # Processamento e classificação de campos
│  │  └─ field_extraction.py
│  ├─ export/                # Exportação em JSON ou banco de dados
│  │  └─ export_json.py
│  ├─ utils/                 # Funções auxiliares
│  │  └─ helpers.py
│  └─ dashboard/             # Interface Streamlit
│     └─ app.py
│
├─ notebooks/                # EDA de OCR e testes de NLP
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ params.yaml               # Configurações do OCR e NLP
└─ README.md
```

---

## **Tecnologias e Bibliotecas**

* **Python 3.10+**
* **OCR**: Tesseract OCR (`pytesseract`) ou PaddleOCR
* **Computer Vision**: OpenCV, Pillow
* **NLP/Transformers**: Hugging Face Transformers (BERT, RoBERTa)
* **Data Handling**: Pandas, Numpy
* **Visualização**: Matplotlib, Seaborn, Plotly
* **Dashboard**: Streamlit
* **Deployment**: Docker + Docker Compose

---

## **Funcionalidades**

1. Carregamento de imagens de documentos via diretório ou interface web.
2. Pré-processamento das imagens (grayscale, binarização, remoção de ruído).
3. Extração de texto usando OCR.
4. Classificação e extração de campos relevantes usando Transformers.
5. Exportação dos resultados em JSON estruturado.
6. Dashboard interativo com upload, visualização de OCR e campos extraídos.

---

## **Pipeline de Desenvolvimento**

1. **Upload e armazenamento das imagens**:

   * Salvar em `data/raw/`.

2. **Pré-processamento das imagens**:

   * Conversão para tons de cinza, binarização e redimensionamento.
   * Remoção de ruído com OpenCV.

3. **Extração de texto via OCR**:

   * Tesseract OCR ou PaddleOCR.
   * Gerar textos brutos (`data/ocr_output/`).

4. **Processamento de texto com NLP**:

   * Tokenização e embeddings via Transformers.
   * Classificação e extração de campos relevantes.

5. **Validação e limpeza dos dados**:

   * Padronização de formatos (datas, valores, CPFs).

6. **Exportação dos resultados**:

   * JSON estruturado para integração com outros sistemas.

7. **Dashboard Streamlit**:

   * Upload de documentos via web.
   * Visualização do OCR, campos extraídos e exportação em JSON.

---

## **Como Rodar Localmente**

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/visionocr-project.git
cd visionocr-project
```

### 2. Criar e ativar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Colocar imagens de documentos

* Salvar em `data/raw/`

### 5. Executar scripts de teste

```bash
python src/data_loader/load_images.py
python src/preprocessing/image_preprocessing.py
python src/ocr/extract_text.py
python src/nlp/field_extraction.py
python src/export/export_json.py
```

### 6. Rodar Dashboard Streamlit

```bash
streamlit run src/dashboard/app.py
```

---

## **Deploy com Docker**

1. Build da imagem:

```bash
docker build -t visionocr:latest .
```

2. Rodar via Docker Compose:

```bash
docker-compose up --build
```

3. Acesse o dashboard: `http://localhost:8501`

---

## **Contribuição**

1. Fork do repositório
2. Criar branch: `git checkout -b feature/nome-feature`
3. Commit: `git commit -m "Descrição da feature"`
4. Push: `git push origin feature/nome-feature`
5. Abrir Pull Request

---

## **Autor**

* **Clayton** – [GitHub](https://github.com/cl4y70n)

---

Quer que eu faça isso agora?
