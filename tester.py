import apisecrets
from gradio_client import Client
import random
import string

seed = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
prompt = apisecrets.promptgenerate()

print(prompt)
print(seed)

client = Client("http://127.0.0.1:7865/", serialize=False)
result = client.predict(
	prompt,	# str in 'parameter_10' Textbox component
	"",	# str in 'Negative Prompt' Textbox component
	["Fooocus V2","Fooocus Enhance","Fooocus Sharp","Fooocus Photograph"],	# List[str] in 'Selected Styles' Checkboxgroup component
	"Speed",	# str in 'Performance' Radio component
	"1152×896", # <span style='color: grey;'> | 1:2</span>",	# str in 'Aspect Ratios' Radio component
	2,	# int | float (numeric value between 1 and 32)in 'Image Number' Slider component
	"12323432243234",	# str in 'Seed' Textbox component
	2,	# int | float (numeric value between 0.0 and 30.0)in 'Image Sharpness' Slider component
	4,	# int | float (numeric value between 1.0 and 30.0)in 'Guidance Scale' Slider component
	"juggernautXL_version6Rundiffusion.safetensors",	# str (Option from: ['juggernautXL_version6Rundiffusion.safetensors', 'realisticStockPhoto_v10.safetensors', 'bluePencilXL_v050.safetensors', 'DreamShaper_8_pruned.safetensors'])in 'Base Model (SDXL only)' Dropdown component
	"None",	# str (Option from: ['None', 'juggernautXL_version6Rundiffusion.safetensors', 'realisticStockPhoto_v10.safetensors', 'bluePencilXL_v050.safetensors', 'DreamShaper_8_pruned.safetensors'])in 'Refiner (SDXL or SD 1.5)' Dropdown component
	0.11,	# int | float (numeric value between 0.1 and 1.0)in 'Refiner Switch At' Slider component
	"None",	# str (Option from: ['None', 'sd_xl_offset_example-lora_1.0.safetensors', 'SDXL_FILM_PHOTOGRAPHY_STYLE_BetaV0.4.safetensors', 'sdxl_lcm_lora.safetensors'])in 'LoRA 1' Dropdown component
	-2,	# int | float (numeric value between -2 and 2)in 'Weight' Slider component
	"None",	# str (Option from: ['None', 'sd_xl_offset_example-lora_1.0.safetensors', 'SDXL_FILM_PHOTOGRAPHY_STYLE_BetaV0.4.safetensors', 'sdxl_lcm_lora.safetensors'])in 'LoRA 2' Dropdown component
	-2,	# int | float (numeric value between -2 and 2)in 'Weight' Slider component
	"None",	# str (Option from: ['None', 'sd_xl_offset_example-lora_1.0.safetensors', 'SDXL_FILM_PHOTOGRAPHY_STYLE_BetaV0.4.safetensors', 'sdxl_lcm_lora.safetensors'])in 'LoRA 3' Dropdown component
	-2,	# int | float (numeric value between -2 and 2)in 'Weight' Slider component
	"None",	# str (Option from: ['None', 'sd_xl_offset_example-lora_1.0.safetensors', 'SDXL_FILM_PHOTOGRAPHY_STYLE_BetaV0.4.safetensors', 'sdxl_lcm_lora.safetensors'])in 'LoRA 4' Dropdown component
	-2,	# int | float (numeric value between -2 and 2)in 'Weight' Slider component
	"None",	# str (Option from: ['None', 'sd_xl_offset_example-lora_1.0.safetensors', 'SDXL_FILM_PHOTOGRAPHY_STYLE_BetaV0.4.safetensors', 'sdxl_lcm_lora.safetensors'])in 'LoRA 5' Dropdown component
	-2,	# int | float (numeric value between -2 and 2)in 'Weight' Slider component
	True,	# bool in 'Input Image' Checkbox component
	prompt,	# str in 'parameter_73' Textbox component
	"Disabled",	# str in 'Upscale or Variation:' Radio component
	"data:base/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==",	# str (filepath or URL to image)in 'Drag above image to here' Image component
	["Left"],	# List[str] in 'Outpaint Direction' Checkboxgroup component
	"data:base/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==",	# str (filepath or URL to image)in 'Drag above image to here' Image component
	" ",	# str in 'Inpaint Additional Prompt' Textbox component
	"data:base/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==",	# str (filepath or URL to image)in 'Image' Image component
	0.9,	# int | float (numeric value between 0.0 and 1.0)in 'Stop At' Slider component
	1.6,	# int | float (numeric value between 0.0 and 2.0)in 'Weight' Slider component
	"ImagePrompt",	# str in 'Type' Radio component
	"data:base/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==",	# str (filepath or URL to image)in 'Image' Image component
	0,	# int | float (numeric value between 0.0 and 1.0)in 'Stop At' Slider component
	0,	# int | float (numeric value between 0.0 and 2.0)in 'Weight' Slider component
	"ImagePrompt",	# str in 'Type' Radio component
	"data:base/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==",	# str (filepath or URL to image)in 'Image' Image component
	0,	# int | float (numeric value between 0.0 and 1.0)in 'Stop At' Slider component
	0,	# int | float (numeric value between 0.0 and 2.0)in 'Weight' Slider component
	"ImagePrompt",	# str in 'Type' Radio component
	"data:base/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==",	# str (filepath or URL to image)in 'Image' Image component																			  
	0,	# int | float (numeric value between 0.0 and 1.0)in 'Stop At' Slider component																  
	0,	# int | float (numeric value between 0.0 and 2.0)in 'Weight' Slider component
	"ImagePrompt",	# str in 'Type' Radio component
	fn_index=29
)
print(result)
