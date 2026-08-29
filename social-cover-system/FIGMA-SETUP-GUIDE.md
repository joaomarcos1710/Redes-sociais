# 🎨 GUIA DE SETUP FIGMA | COMPONENTES PROFISSIONAIS

Como estruturar seu arquivo Figma para criar capas profissionais usando os templates do sistema.

---

## 🎯 OBJETIVO

Transformar os **10 templates SVG** em **componentes Figma reutilizáveis** com:
- Textos editáveis
- Fotos substituíveis
- Cores variáveis (light/dark)
- Estados diferentes (hover, active)
- Componentes aninhados

---

## 📋 ESTRUTURA RECOMENDADA PARA SEU FIGMA

```
📁 Social Cover System | João Marcos
│
├─ 📂 SISTEMA
│  ├─ Cores
│  ├─ Tipografia
│  ├─ Componentes Base
│  └─ Grid de Referência
│
├─ 📂 TEMPLATES (10 arquivos)
│  ├─ 01-Editorial
│  ├─ 02-Photographic
│  ├─ 03-Typographic
│  ├─ 04-Text-on-Photo
│  ├─ 05-Split-Screen
│  ├─ 06-Minimal
│  ├─ 07-Headline-Gigante
│  ├─ 08-Lista
│  ├─ 09-Citação
│  └─ 10-Story-Cinematico
│
├─ 📂 COMPONENTES REUTILIZÁVEIS
│  ├─ Headlines
│  │  ├─ Headline-XL
│  │  ├─ Headline-LG
│  │  ├─ Headline-MD
│  │  └─ Headline-Red
│  ├─ Overlays
│  │  ├─ Overlay-Light
│  │  ├─ Overlay-Medium
│  │  └─ Overlay-Dark
│  ├─ Elementos
│  │  ├─ Linha-Red
│  │  ├─ Assinatura
│  │  └─ Badge-Categoria
│  └─ Backgrounds
│     ├─ Black-Base
│     └─ Pattern-Subtle
│
├─ 📂 CATEGORIAS (11 pastas)
│  ├─ Teologia
│  ├─ Corrida
│  ├─ CrossFit
│  ├─ Natação
│  ├─ Saúde
│  ├─ Finanças
│  ├─ Tecnologia
│  ├─ Viagens
│  ├─ Pessoal
│  ├─ Reflexões
│  └─ Mix
│
├─ 📂 EXEMPLOS (30+ capas criadas)
│  ├─ Exemplo-01-Editorial-Teologia
│  ├─ Exemplo-02-Fotografico-Corrida
│  └─ ... (um para cada tipo + pilar)
│
├─ 📂 GRID VISUAL
│  ├─ Grid-3x3-Mix-01
│  ├─ Grid-3x3-Mix-02
│  └─ Grid-3x3-Mix-03
│
└─ 📂 REFERÊNCIA
   ├─ Design-System-Visual
   ├─ Typography-Scale
   ├─ Color-Palette
   └─ Spacing-Grid
```

---

## 🚀 PASSO A PASSO: DO SVG AO COMPONENTE FIGMA

### PASSO 1: IMPORTAR SVG COMO BASE

**No seu Figma:**

```
1. Abrir arquivo do Figma
2. Menu Assets > Import
3. Selecionar: templates/01-editorial.svg
4. Figma vai importar como frame
5. Adicionar ao painel Assets > Components
```

### PASSO 2: ESTRUTURAR O TEMPLATE

Depois que importar o SVG (agora é um frame):

**Renomear layers:**
```
Frame "01-Editorial" 
├─ Background (rect preta)
├─ Photo-Placeholder (rect cinza)
├─ Overlay-Gradient (uso de máscara)
├─ Content
│  ├─ Line-Red (rect vermelha 4px)
│  ├─ Headline (texto)
│  ├─ Subtitle (texto)
│  └─ Signature (texto)
└─ Safe-Area-Guide (apenas guia, não exportar)
```

### PASSO 3: CRIAR COMPONENTES DOS ELEMENTOS

**Headline Componente:**
```
1. Selecionar texto "HEADLINE" 
2. Right-click > Create component
3. Renomear: "Headline / XL"
4. No painel direita, adicionar properties:
   - Text: "Editar texto"
   - Color: branco / vermelho
   - Size: 140px / 180px / 200px
```

**Overlay Componente:**
```
1. Selecionar gradient overlay
2. Right-click > Create component
3. Renomear: "Overlay / Editorial"
4. Properties:
   - Opacity: Light (20%) / Medium (35%) / Dark (50%)
```

**Linha Vermelha Componente:**
```
1. Selecionar rect 4px vermelho
2. Right-click > Create component
3. Renomear: "Divider / Red"
4. Properties:
   - Visible: true/false
   - Width: 80px / 100px / 120px
```

### PASSO 4: CRIAR COMPONENTE DO TEMPLATE COMPLETO

**Editorial Template como Componente:**

```
1. Selecionar frame completo "01-Editorial"
2. Right-click > Create component
3. Renomear: "Template / Editorial"
4. No painel Assets, ver component criado
```

**Properties do Template:**

```
Variant "Photo-Position":
├─ Top (foto até 40% de cima)
├─ Center (foto centralizada)
└─ Bottom (foto até 40% de baixo)

Variant "Content-Position":
├─ Top (conteúdo em cima)
├─ Center (conteúdo centralizado)
└─ Bottom (conteúdo em baixo)

Variant "Color-Theme":
├─ Dark (preto base)
├─ Light (cinza escuro base)

Variant "Has-Divider":
├─ true
└─ false
```

---

## 💡 COMPONENTES PRINCIPAIS A CRIAR

### 1. **Headline Component**
```
Name: "Headline"
Variants:
- Size: XL (200px) / LG (140px) / MD (100px)
- Color: White / Red
- Transform: CAPS / Title
- Font: League Gothic
```

**Uso**: Em qualquer template, arrastar e renomear

### 2. **Subtitle Component**
```
Name: "Subtitle"
Variants:
- Size: LG (32px) / MD (24px) / SM (18px)
- Color: Off-White / Gray-Light
- Font: Montserrat
```

### 3. **Overlay Component**
```
Name: "Overlay"
Variants:
- Intensity: None / Light (20%) / Medium (35%) / Dark (50%)
- Color: Black / White
```

### 4. **Photo Frame Component**
```
Name: "PhotoFrame"
Variants:
- Aspect-Ratio: 1080x1350 / 1080x1920 / 540x1350
- Border: None / Guide (traço vermelho)
- Placeholder: Show / Hide
```

### 5. **Divider Component**
```
Name: "Divider"
Variants:
- Color: Red / Gray
- Width: 80px / 100px / 120px
- Opacity: Full / Subtle (40%)
```

### 6. **Signature Component**
```
Name: "Signature"
Variants:
- Position: Bottom-Left / Bottom-Right / Top-Right
- Color: Gray-Medium / Gray-Dark
- Visible: true / false
```

---

## 📐 VARIAÇÕES DE TEMPLATES

Cada template deve ter componentes aninhados com variações:

### Template: Editorial
```
Variants:
└─ Photo-Opacity
   ├─ Light (20% overlay)
   ├─ Medium (40% overlay)
   └─ Dark (60% overlay)

└─ Text-Position
   ├─ Bottom (texto embaixo)
   ├─ Middle (texto meio da foto)
   └─ Overlay (texto sobre foto)

└─ Content-Style
   ├─ Simple (só headline)
   ├─ Standard (headline + subtitle)
   └─ Rich (headline + subtitle + divider)
```

### Template: Tipográfico
```
Variants:
└─ Color-Scheme
   ├─ Dark (fundo preto)
   ├─ Gray (fundo cinza)
   └─ Light (fundo off-white)

└─ Highlight
   ├─ None
   ├─ Red-Word (palavra em vermelho)
   └─ Red-Line (linha vermelha)

└─ Spacing
   ├─ Tight (menos espaço)
   ├─ Normal (normal)
   └─ Relaxed (mais espaço)
```

---

## 🎯 FLUXO DE USO NO FIGMA

### Criar uma capa nova:

```
1. ARRASTAR template component
   → Figma > Assets > Templates > Editorial
   → Drag to canvas

2. ESCOLHER variações
   → Photo-Opacity: Dark
   → Text-Position: Bottom
   → Content-Style: Standard

3. EDITAR TEXTOS
   → Duplo clique no headline
   → Digitar novo texto
   → Figma auto-ajusta (se texto não fixo)

4. TROCAR FOTO
   → Selecionar Photo-Frame
   → Right-click > Fill > Image > Upload

5. CUSTOMIZAR CORES (se necessário)
   → Selecionar elemento
   → Painel direita > Fill > escolher cor do token

6. EXPORTAR
   → Right-click > Export
   → PNG, scale 1x
   → 1080×1350 ou 1080×1920
```

---

## 🔧 SETUP DE TOKENS (Cores e Tipografia)

### Criar Tokens de Cor

**No Figma:**
```
Menu: Assets > Colors (ou ícone de cor)

Criar tokens:
├─ Primary
│  ├─ Black: #0E0E0E
│  ├─ White: #FFFFFF
│  ├─ Off-White: #F5F4F2
│  └─ Red: #E5341E
├─ Gray
│  ├─ Dark: #2A2A2A
│  ├─ Medium: #4A4A4A
│  └─ Light: #AEAEAE
```

**Usar em componentes:**
```
1. Selecionar elemento
2. Painel direita > Fill
3. Clicar na cor > Adicionar a library
4. Usar token: "Primary / Red"
```

### Criar Tokens de Tipografia

**No Figma:**
```
Menu: Assets > Typography

Criar estilos:
├─ Headline / XL
│  ├─ Font: League Gothic
│  ├─ Size: 200px
│  ├─ Weight: 700
│  ├─ Tracking: +2
│  └─ Transform: CAPS
├─ Headline / LG
│  └─ (140px, similar)
└─ Body / Regular
   ├─ Font: Montserrat
   ├─ Size: 18px
   └─ Weight: 400
```

---

## 📊 EXEMPLO: CRIAR CAPA EDITORIAL EM FIGMA

**Resumo do workflow:**

```
1. BUSCAR TEMPLATE
   Assets > Templates > Editorial
   Arrastar para canvas

2. VARIAÇÕES
   Component > Photo-Opacity: Dark
   Component > Text-Position: Bottom

3. EDITAR
   Duplo clique headline > "CORRA POR PROPÓSITO"
   Duplo clique subtitle > "Uma reflexão sobre movimento"

4. FOTO
   Select Photo-Frame > Fill > Image > Upload foto.jpg

5. CORES
   Headline > Fill > usar token "Primary/Red" (se quiser vermelho)

6. EXPORT
   Right-click > Export PNG > 1080×1350

7. PRONTO!
```

**Tempo total**: ~10 minutos

---

## 🚀 SETUP RECOMENDADO (PASSO A PASSO)

### DIA 1: INFRAESTRUTURA
```
[ ] Criar arquivo Figma "Social Cover System | João Marcos"
[ ] Criar seção SISTEMA
[ ] Importar todos os 10 SVGs como frames
[ ] Organizar em frames nomeadas
```

### DIA 2: COMPONENTES
```
[ ] Criar componentes base (Headline, Subtitle, Overlay)
[ ] Criar componentes de elementos (Divider, Signature, Photo)
[ ] Criar tokens de cor
[ ] Criar estilos de tipografia
```

### DIA 3: TEMPLATES
```
[ ] Criar componentes para os 10 templates
[ ] Adicionar variações principais
[ ] Testar drag-and-drop
[ ] Otimizar estrutura
```

### DIA 4: EXEMPLOS E DOCUMENTAÇÃO
```
[ ] Criar 3 exemplos usando cada template
[ ] Criar grid visual 3×3
[ ] Documentar como usar no README do Figma
[ ] Testar fluxo completo
```

---

## 💎 MELHORES PRÁTICAS FIGMA

### Nomeação de Componentes
```
✅ BOM:
Template / Editorial
Headline / XL
Overlay / Medium

❌ EVITAR:
template1
headline big
overlay_v2
```

### Organização de Variantes
```
✅ BOM:
Component / Variant-Group / Option
Template / Editorial / Photo-Opacity / Dark

❌ EVITAR:
Template_Editorial_Dark_v2
Editorial - Dark Overlay
```

### Estrutura de Layers
```
✅ BOM:
Component-Name
├─ Background
├─ Photo
├─ Content
│  ├─ Headline
│  ├─ Subtitle
│  └─ Elements
└─ Guides (desabilitar para export)

❌ EVITAR:
Group 1
├─ Shape
├─ Text 1
├─ Text 2
└─ Rectangle 3
```

---

## 📱 EXPORT SETTINGS

**Para Instagram Feed:**
```
Seleção: Frame 1080×1350
Export:
- Format: PNG
- Scale: 1x
- Suffix: @1x
```

**Para Reels/Stories:**
```
Seleção: Frame 1080×1920
Export:
- Format: PNG
- Scale: 1x
- Suffix: @1x
```

**Para Web Preview:**
```
Export:
- Format: PNG
- Scale: 2x (para tela de alta DPI)
```

---

## 🎯 CHECKLIST DE SETUP COMPLETO

```
[ ] Arquivo Figma criado
[ ] 10 templates importados como frames
[ ] Componentes base criados (Headline, Subtitle, Overlay)
[ ] Componentes de elementos criados (Divider, Photo, Signature)
[ ] Tokens de cor configurados
[ ] Estilos de tipografia configurados
[ ] Variantes de templates criadas
[ ] 3 exemplos completos criados
[ ] Grid visual testada
[ ] Export settings configurados
[ ] Documentação adicionada
[ ] Fluxo completo testado
```

---

## 📞 TROUBLESHOOTING FIGMA

### SVG não importa direito
→ Certifique-se que SVG está bem formado
→ Tente copiar/colar o conteúdo SVG diretamente

### Textos não ficam editáveis
→ Verificar se é texto de verdade (não path)
→ Right-click > Convert to text

### Componentes não sincronizam
→ Main component deve estar na seção "Components"
→ Instances puxam mudanças automaticamente

### Muito lento ao trocar componentes
→ Reduzir número de variantes
→ Usar linked components ao invés de nested

---

## 🎨 PRÓXIMO: USAR O FIGMA

Depois de setup completo:

1. **Arquivo Figma pronto** com componentes reutilizáveis
2. **Componentizacao** permite criar capas em < 10 min
3. **Variações** garantem consistência
4. **Export** direto para Instagram/TikTok
5. **Escalável** para 365+ capas

---

## 📚 RECURSOS

- [Figma Components Guide](https://www.figma.com/design-systems/) (oficial Figma)
- Design System criado: `DESIGN-SYSTEM.md`
- Exemplos práticos: `EXEMPLOS-PRATICOS.md`
- Templates base: `templates/` (SVG originais)

---

**Status**: Guia completo de setup Figma | Pronto para implementar
