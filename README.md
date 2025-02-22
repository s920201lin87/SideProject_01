# Flask x MongoDB 會員系統

這是一個使用 **Python Flask** 與 **MongoDB** 打造的會員管理系統，實作了使用者註冊、登入、登出與 Session 機制，達到基本的會員功能。

---

## 功能與特色

1. **會員登入**  
   - 透過表單收集信箱與密碼，與資料庫進行比對。  
   - 登入成功後，使用 Session 儲存使用者資訊。

2. **會員註冊**  
   - 以表單收集使用者名稱、信箱與密碼。  
   - 新增至 MongoDB 資料庫，並預防重複信箱註冊。

3. **Session 管理**  
   - 使用 Flask 內建的 Session 機制進行登入狀態維護。  
   - 登出時清除 Session。

4. **錯誤訊息處理**  
   - 登入或註冊失敗時（找不到使用者或密碼錯誤、信箱重複），導向錯誤頁面顯示提示訊息。

---



