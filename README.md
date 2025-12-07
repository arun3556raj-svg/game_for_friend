# Number Guessing Game — Web version

This is a single-file HTML conversion of the Python guessing game. Save `index.html` and host it anywhere that serves static files to get a sharable URL.

Quick hosting options:
- GitHub Pages
  1. Create a repository (or use an existing one).
  2. Add `index.html` to the repository root on the default branch (`main` or `master`).
  3. In repo Settings → Pages, set "Source" to the branch and root folder. Save.
  4. GitHub Pages will publish at `https://<username>.github.io/<repo>/` (or the repo slug) — use that as the shareable URL.

- raw.githack (fast direct preview)
  1. Push `index.html` to a GitHub repo.
  2. Get the raw GitHub URL to the file, e.g. `https://raw.githubusercontent.com/<user>/<repo>/<branch>/index.html`
  3. Visit https://raw.githack.com/ and paste the raw URL — it gives a CDN URL you can share.

- Netlify Drop
  1. Zip `index.html` and drop it on https://app.netlify.com/drop
  2. Netlify will give you a public URL instantly.

- Any static host
  Upload `index.html` to any static web host (Vercel, Firebase Hosting, Surge, etc).

Notes
- The page is a self-contained client-side implementation (no server required).
- The "Copy shareable URL" button copies the current page URL (works best once hosted).
- To keep friend-specific state (e.g., preset name in URL) we can add simple URL params — tell me if you want name/difficulty encoded in the link.

If you want, I can:
- Create a repository with this file and (optionally) enable GitHub Pages for you.
- Add a small meta preview image and nicer styling.
- Add URL parameters so you can pre-fill the player's name/difficulty and share a link that preloads them.

Which of these would you like me to do next?