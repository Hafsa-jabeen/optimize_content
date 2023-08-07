from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import os

openai.api_key = os.environ.get('OPEN_AI_KEY')

def index(request):
  return render(request,"seoapp/index.html")

@csrf_exempt
def optimize(request):
    if request.method == 'POST':
        content = request.POST['content']
        output_text = optimize_with_chatgpt(content)
        return HttpResponse(output_text)

def optimize_with_chatgpt(content):
    response = openai.Completion.create(
        engine="davinci",  # You can experiment with different engines
        prompt=content,
        max_tokens=1000  # Adjust this based on your desired length
    )
    optimized_content = response.choices[0].text.strip()
    return optimized_content