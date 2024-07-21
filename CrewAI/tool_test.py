from crewai_tools import ScrapeWebsiteTool

# To enable scrapping any website it finds during its execution
tool = ScrapeWebsiteTool()

# Initialize the tool with the website URL, so the agent can only scrap the content of the specified website
tool = ScrapeWebsiteTool(website_url='https://www.nike.com/kr/t/%EC%A1%B0%EB%8D%98-%EC%97%90%EC%84%BC%EC%85%9C-%EB%82%A8%EC%84%B1-%EC%9A%B0%EB%B8%90-%ED%8C%AC%EC%B8%A0-h5XkOrQN/DQ7509-010')

# Extract the text from the site
text = tool.run()
print(text)