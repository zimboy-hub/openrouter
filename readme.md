# Openrouter
OpenRouter is a unified AI routing platform and API marketplace that lets developers access hundreds of large language models (LLMs) through a single API key and interface.

Key Features

- Single API Key: Instead of setting up separate accounts, billing, and SDKs for providers like OpenAI, Anthropic, Google, and DeepSeek, developers use one OpenRouter account and key. 
- Model Flexibility: Users can switch between hundreds of proprietary and open-weight models simply by changing the model name in their code. 
- Smart Routing & Fallbacks: The platform routes requests based on a mix of price, speed, and reliability, and automatically falls back to secondary providers if a primary API goes down. 
- OpenAI-Compatible: Its API mimics OpenAI's format, making it easy to plug into existing codebases, LLM tools, and coding agents (such as Claude Code, Cursor, and Zed). 
- Free & Paid Tiers: It offers access to select free-to-use models as well as pay-as-you-go pricing for commercial and high-performance models. 
Originally founded in 2023, OpenRouter was acquired by Stripe in 2026 to help scale token routing and usage optimization for businesses.

# Installation
To access OpenRouter in Python, the easiest and cleanest way is to use the official openai library. Because OpenRouter is fully compatible with the OpenAI API format, you only need to change your base_url to point to OpenRouter's servers and provide your OpenRouter API key.

Install the OpenAI library
pip install openai

## Pro-Tip: Managing your API Key securely

Instead of hardcoding your API key directly into the script, it is best practice to set it as an environment variable in your Windows environment:

    In Windows PowerShell: $env:OPENROUTER_API_KEY="your_actual_api_key"
    The script will automatically pick it up via os.environ.get("OPENROUTER_API_KEY").

# Free models available (Nov 2026)
Aside from Google's Gemma 4 models, OpenRouter offers around 15 to 20 free open-weights and preview models (all ending with the :free suffix), led by NVIDIA's Nemotron 3/3.5 series, Baidu's ERNIE 5.5 Flash, Dots3-Note Preview, and Cohere North Mini Code. 

Top Free Models by Use Case

You can pass any of these slugs into your model parameter: 

• Heavy Reasoning & Large Context:
	• nvidia/nemotron-3-ultra-550b-a55b:free — 550B parameter model with a massive 1M token context window.
	• nvidia/nemotron-3.5-lightning:free — High-speed reasoning model with a 1M token context window. 
• Vision & Multimodal (Images/Video/Audio):
	• nvidia/nemotron-3.5-super-vl:free — Supports text, image, and video inputs with a 1M token context window.
	• nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free — Accepts text, image, audio, and video inputs (256K context). 
• General Chat & Long-Form Output:
	• dots-studio/dots-3-note-preview:free — 512K context window with high output limits and no prompt training.
	• baidu/ernie-5.5-flash-preview:free — Fast general-purpose preview model. 
• Coding & Lightweight Tasks:
	• cohere/north-mini-code:free — Specialized for programming tasks (256K context).
	• liquid/lfm-3-1.7b:free — Ultra-lightweight, fast model for simple text tasks (262K context).

## Key Limits & Caveats

• Rate Limits: Free :free models are capped at 20 requests per minute and 50 requests per day on unfunded accounts. Purchasing at least $10 in lifetime credits raises the daily free limit to 1,000 requests per day (without spending your credits on free calls). 
• Data Privacy: Several free providers (including NVIDIA and Liquid) may use prompts submitted to :free endpoints to train their models. Avoid sending sensitive code or private data.
• Rotation: OpenRouter regularly rotates preview models in and out. You can verify live availability anytime on the OpenRouter Free Models Collection.
What is your primary use case (such as coding, multimodal vision, or general chat), so I can recommend the most reliable model slug and help you set up fallback routing?
