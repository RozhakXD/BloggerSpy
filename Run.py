try:
    import requests, re, json, time, os, sys, string, random
    from rich.console import Console
    from rich.panel import Panel
    from rich import print as Print
    from requests.exceptions import RequestException
except ModuleNotFoundError:
    print("Please Install Module Requests & Rich")
    exit()

FILE_NAME = {
    "Name": "Temporary/Results.txt",
}

def Banner() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    Print(
        Panel(
            r"""[bold magenta] ______ _                             _____             
 | ___ \ |                           /  ___|            
 | |_/ / | ___   __ _  __ _  ___ _ __\ `--. _ __  _   _ 
 | ___ \ |/ _ \ / _` |/ _` |/ _ \ '__|`--. \ '_ \| | | |
 | |_/ / | (_) | (_| | (_| |  __/ |  /\__/ / |_) | |_| |
 \____/|_|\___/ \__, |\__, |\___|_|  \____/| .__/ \__, |
                 __/ | __/ |               | |     __/ |
[bold magenta]                |___/ |___/                |_|    |___/
     [underline red]Extract, Analyze, and Reveal Blogger Insights""", width=61, style="bold bright_yellow"
        )
    )

def Fitur() -> None:
    try:
        Banner()
        Print(
            Panel(f"[bold white]Please Fill In The Blogger Category, You Can Fill In The \"[bold green]LIST[bold white]\" To Display The Most Popular Categ\nories *[bold red]Use Only One Category For Satisfactory Results[bold white]!", width=61, style="bold bright_yellow", title="[bold bright_yellow]>> [Category] <<", subtitle="[bold bright_yellow]╭───────", subtitle_align="left")
        )
        category = Console().input("[bold bright_yellow]   ╰─> ")
        if category.lower() == "list":
            with open("Penyimpanan/Category.json", "r") as f:
                data = json.load(f)
                Print(
                    Panel(f"[bold green]{str(data['Name']).replace('[', '').replace(']', '')}", width=61, style="bold bright_yellow")
                )
                Print(
                    Panel(f"[bold white]You Can Choose One And Do Copy Then Repeat This Program So You Can Enter Category!", width=61, style="bold bright_yellow", title="[bold bright_yellow]>> [Notes] <<")
                )
            sys.exit()
        else:
            FILE_NAME["Name"] = 'Temporary/' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + ".txt"
            Print(
                Panel(f"[bold white]You Can Use[bold red] CTRL + C[bold white] If You Want To Stop. For Maximum Results Use Popular Categories!", width=61, style="bold bright_yellow", title="[bold bright_yellow]>> [Notes] <<")
            )
            try:
                Search_Blogger(category)
            except KeyboardInterrupt:
                Print(f"[bold bright_yellow]   ──>[bold red] PROGRAM STOPPED!      ", end="\r")
                time.sleep(2)
            Print(
                Panel(f"[bold white]Congratulations! You Have Successfully Collected All Blog\ns With Category \"[bold green]{category}[bold white]\" And For The\nResults We Have Saved In File[bold red] {FILE_NAME['Name']}", width=61, style="bold bright_yellow", title="[bold bright_yellow]>> [Completed] <<")
            )
            sys.exit()
    except Exception as e:
        Print(Panel(f"[bold red]{str(e).title()}", width=61, style="bold bright_yellow", title="[bold bright_yellow]>> [Error] <<"))
        sys.exit()

def Search_Blogger(category: str) -> None:
    try:
        with requests.Session() as session:
            session.headers.update({
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "www.google.com",
                "sec-ch-prefers-color-scheme": "dark",
                "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
                "sec-ch-ua-mobile": "?0",
                "Accept-Encoding": "gzip, deflate",
                "sec-ch-ua-platform": "\"Windows\"",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                "X-Browser-Channel": "stable",
                "X-Browser-Copyright": "Copyright 2025 Google LLC. All rights reserved.",
                "X-Browser-Validation": "1nAW9Rb/M8Lkk97ILDg00FWYjns=",
                "X-Browser-Year": "2025",
                "X-Client-Data": "CKWWywE="
            })
            params = {
                'oq': f'site:blogger.com/profile {category}',
                'sourceid': 'chrome',
                'gs_lcrp': '',
                'ie': 'UTF-8',
                'q': f'site:blogger.com/profile {category}'
            }
            response = session.get('https://www.google.com/search?', params=params, allow_redirects=True)
            data = list(set(re.findall(r"https:\/\/www\.blogger\.com\/profile\/\d+", response.text)))
            for profile in data:
                profile_id = profile.split("/")[-1]
                Print(f"[bold bright_yellow]   ──>[bold green] VISIT #{profile_id}!      ", end="\r")
                time.sleep(2)
                Get_Blogger_Profile(profile_urls=profile)
            if "\"sca_esv\"" in response.text and "ei=" in response.text:
                Print(f"[bold bright_yellow]   ──>[bold green] NEXT CURSOR SUCCESSFULLY FOUND!", end="\r")
                time.sleep(2)
                sca_esv = re.search(r'name="sca_esv" value="(.+?)"', response.text).group(1)
                ei = re.search(r'ei=(.+?)&amp;', response.text).group(1)
                Next_Search_Blogger(session, category, sca_esv, ei, start=10)
                return None
            else:
                Print(f"[bold bright_yellow]   ──>[bold red] NEXT PAGE NOT FOUND!      ", end="\r")
                time.sleep(2)
                return None
    except RequestException:
        Print(f"[bold bright_yellow]   ──>[bold red] CONNECTION ERROR!      ", end="\r")
        time.sleep(2)
        Search_Blogger(category)

def Next_Search_Blogger(session: requests.Session, category: str, sca_esv: str, ei: str, start: int) -> None:
    try:
        params = {
            'q': f'site:blogger.com/profile {category}',
            'sca_esv': sca_esv,
            'ei': ei,
            'start': start,
            'sa': 'N'
        }
        session.headers.update({
            "Referer": "https://www.google.com/search?",
            "Sec-Fetch-Site": "same-origin",
        })
        response = session.get('https://www.google.com/search?', params=params, allow_redirects=False)
        data = list(set(re.findall(r"https:\/\/www\.blogger\.com\/profile\/\d+", response.text)))
        for profile in data:
            profile_id = profile.split("/")[-1]
            Print(f"[bold bright_yellow]   ──>[bold green] VISIT #{profile_id}!      ", end="\r")
            time.sleep(2)
            Get_Blogger_Profile(profile_urls=profile)
        if "\"sca_esv\"" in response.text and "ei=" in response.text:
            Print(f"[bold bright_yellow]   ──>[bold green] NEXT CURSOR SUCCESSFULLY FOUND!", end="\r")
            time.sleep(2)
            sca_esv = re.search(r'name="sca_esv" value="(.+?)"', response.text).group(1)
            ei = re.search(r'ei=(.+?)&amp;', response.text).group(1)
            Next_Search_Blogger(session, category, sca_esv, ei, start=start+10)
            return None
        else:
            Print(f"[bold bright_yellow]   ──>[bold red] NEXT PAGE NOT FOUND!      ", end="\r")
            time.sleep(2)
            return None
    except RequestException:
        Print(f"[bold bright_yellow]   ──>[bold red] CONNECTION ERROR!      ", end="\r")
        time.sleep(2)
        Next_Search_Blogger(session, category, sca_esv, ei, start)

def Get_Blogger_Profile(profile_urls: str) -> None:
    try:
        with requests.Session() as session:
            session.headers.update({
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Sec-Fetch-Dest": "document",
                "Host": "www.blogger.com",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Connection": "keep-alive",
                "Sec-Fetch-Mode": "navigate",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
            })
            response = session.get("{}".format(profile_urls), allow_redirects=True)

            joined = re.search(r"Di Blogger sejak\s+([A-Za-z]+\s\d{4})", response.text)
            name = re.search(r"<h1>(.*?)<\/h1>", response.text)
            views = re.search(r"Tampilan profil\s*-\s*(\d+)", response.text)
            emails = re.findall(r"<div class=\"\">(.*?)<\/div>|mailto:([\w\.-]+@[\w\.-]+\.\w+)", response.text)

            email_list = [email[0] or email[1] for email in emails if any(email)]

            Print(Panel(f"""[bold white][[bold green]*[bold white]] Complete Name: {name.group(1) if name else '[bold red]Tidak ditemukan'}
[bold white][[bold green]*[bold white]] Links:[bold green] {profile_urls}
[bold white][[bold green]*[bold white]] Joined: {joined.group(1) if joined else '[bold red]Tidak ditemukan'}
[bold white][[bold green]*[bold white]] Views: {views.group(1) if views else '[bold red]Tidak ditemukan'}
[bold white][[bold green]*[bold white]] Emails: {email_list if email_list else '[bold red]Tidak ditemukan'}""", width=61, style="bold bright_yellow", title="[bold bright_yellow]>> [Success] <<"))

            with open(f"{FILE_NAME['Name']}", "a") as f:
                f.write(
                    f"{name.group(1) if name else 'Tidak ditemukan'}|{profile_urls}|{joined.group(1) if joined else 'Tidak ditemukan'}|{views.group(1) if views else 'Tidak ditemukan'}|{', '.join(email_list) if email_list else 'Tidak ditemukan'}\n"
                )

            return None
    except RequestException:
        Print(f"[bold bright_yellow]   ──>[bold red] CONNECTION ERROR!      ", end="\r")
        time.sleep(2)
        Get_Blogger_Profile(profile_urls)

if __name__ == '__main__':
    try:
        os.system('git pull')
        Fitur()
    except KeyboardInterrupt:
        sys.exit()