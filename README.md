# *Facebook Page Scraper API*  

A FastAPI-based service to scrape Facebook pages, store details in MongoDB, and expose APIs for fetching page information, posts, followers, and filtering pages by followers count.  

## 🚀 *Features*  
- ✅ *Scrapes Facebook Page details:*  
  - Page Name, URL, Profile Pic, Email, Website, Category, Followers, Likes, Creation Date  
- ✅ *Scrapes and stores:*  
  - Posts (25-40 recent posts)  
  - Comments on posts  
  - Followers & Following details  
- ✅ *Stores scraped data in MongoDB*  
- ✅ *FastAPI-based API with pagination & filtering*  
- ✅ *Includes Postman collection for testing*  

---

## 🛠 *Tech Stack*  
- *Backend:* FastAPI (Python)  
- *Database:* MongoDB Atlas  
- *Web Scraping:* BeautifulSoup, Requests  

---

## 📂 *Project Structure*  
```sh
📁 facebook_scraper_project  
│── dp.py          # Database connection & queries  
│── main.py        # FastAPI server & endpoints  
│── scraper.py     # Scraper service for fetching page details  
│── test.py        # Testing script  
│── .env           # Environment variables (MongoDB URI)  
│── README.md      # Project documentation  
│── requirements.txt  # Dependencies list
