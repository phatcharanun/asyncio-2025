# Assignment

## **Assignment: Async Multi-Server Student Analytics Client**

### **Background**

Your team manages multiple FastAPI servers, each hosting student data for different campuses. Each server exposes the following endpoints:

1. `/students` → returns a list of all students
2. `/analytics/group` → returns the number of students per group
3. `/analytics/year` → returns the number of students per enrolled year

Your task is to develop an **asynchronous Python client** that fetches data from all servers concurrently and displays the results.

---

### **Requirements**

1. **Input**

   * A list of FastAPI server URLs (e.g., `http://server1:8000`, `http://server2:8000`, `http://server3:8000`)

2. **Async Fetch**

   * Use `asyncio` + `httpx.AsyncClient` to fetch data **concurrently**
   * Fetch **all three endpoints** (`/students`, `/analytics/group`, `/analytics/year`) from **all servers**

3. **Processing**

   * For `/students`, display **only the total number of students** per server
   * For `/analytics/group` and `/analytics/year`, display the full response
   * Handle any exceptions gracefully (e.g., server down, timeout)

4. **Output**

   * Print the results in the console in **readable JSON-like format**, e.g.:

```json
{
  "server": "http://server1:8000",
  "student_count": 17
}
{
  "server": "http://server1:8000",
  "group_analytics": [{"group_no":1,"count":4}, {"group_no":2,"count":3}, ...]
}
{
  "server": "http://server1:8000",
  "year_analytics": [{"enrolled_year":2566,"count":12}, ...]
}
```
