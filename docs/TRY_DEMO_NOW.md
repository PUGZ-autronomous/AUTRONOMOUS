# Try AUTRONOMOUS before you get home

You can test the interface this week using a temporary GitHub Codespaces computer in your browser. The home PC remains the planned permanent host. No installation on your travel laptop is needed.

The demo uses simulated execution. It lets you test controls and screens; it does not research a real market or run a business.

## Open the test computer

1. Sign into your GitHub account and open [this demo setup link](https://codespaces.new/PUGZ-autronomous/AUTRONOMOUS/tree/build/autronomous-foundation?quickstart=1).
2. Confirm the repository is PUGZ-autronomous/AUTRONOMOUS and the branch is build/autronomous-foundation. Choose the smallest 2-core machine if a machine selection is offered.
3. Click Create codespace, or resume the existing matching codespace. Wait for the browser editor and dependency setup to finish. You should see "Demo environment ready" in the setup output.
4. In its terminal at the bottom, paste this and press Enter:

```bash
bash scripts/start_demo.sh
```

5. Open the PORTS tab near the terminal. Find port 8799, confirm its visibility is Private, then use Open in Browser (the globe icon) or the forwarded address. Keep it private: the app still relies on the local operator boundary.
6. Use Control room in the app to reach the dashboard. Manual opens the guide. Opening the forwarded app address on your phone should work after signing into the same GitHub account; mobile forwarding/login has not been tested yet.

If setup fails, show the error text or a screenshot with credentials omitted. If the page opens the original upstream interface, check you selected the foundation branch. If you created a codespace before the configuration was added, create a fresh one or rebuild its container.

## Five-minute walkthrough

1. In the control room, confirm DEMO MODE and four demo component rows. All six workers should say planned; revenue should say unconnected.
2. Open Chat and submit "Prepare a checklist for evaluating a digital product idea." Result cards should appear. These are simulated results.
3. Return to Control room and press Pause new runs. Try another command: expect a paused error. Existing admitted work is not cancelled by this button.
4. In the terminal, press Ctrl+C to stop the app, then run bash scripts/start_demo.sh again. The pause should remain. Earlier web run history currently resets; full history persistence is still a build milestone.
5. Press Resume new runs and submit another demo command.

You can also run the automated real-process check from the terminal while the manual demo is stopped:

```bash
.venv/bin/python scripts/smoke_demo.py
```

It uses temporary isolated state, starts two successive web-server processes, checks result cards, pause rejection, restart recovery and resume, then removes its test state. It never activates paid AI components.

## Stop after testing

Stop the server with Ctrl+C. At https://github.com/codespaces use the codespace's menu to Stop codespace; closing the laptop tab is not the same as explicitly stopping compute. Delete the codespace when finished with the experiment if you no longer need its test state. The committed source remains on GitHub.

GitHub personal accounts include a monthly Codespaces allowance. Usage depends on machine size; storage continues counting while a codespace exists, even when stopped. Your remaining allowance has not been checked. Use included usage, and review any billing prompt rather than enabling paid usage for this demo. This test route is optional and is not an always-on production server.

## Home PC check

The ASUS M3402WFA specification lists Ryzen 5 7520U and Ryzen 3 7320U options, both with four cores/eight threads; on-board LPDDR5 comes in 8GB or 16GB variants. SSD capacities include 256GB, 512GB and 1TB. The pasted family specification does not establish which configuration you own.

Our planning judgement: the 16GB version looks suitable for the initial API-backed service and one lightweight worker, subject to actual workload and available memory. An 8GB unit calls for a tighter one-worker setup and measurement. Local AI/model hosting and many concurrent worker desktops are separate sizing questions. Confirm the actual RAM and disk when home; the RAM is on-board, so a conventional RAM-stick upgrade should not be assumed.

## Validation boundary

The demo source, loopback server requests and restart smoke check have been exercised in the development environment. An actual GitHub Codespaces creation, its forwarded login and desktop/mobile visual layout have not been exercised. Those are the next interactive checks when you open it.

## Official references

- [GitHub Codespaces overview](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces)
- [Forwarded ports](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace)
- [Codespaces security and private ports](https://docs.github.com/en/codespaces/reference/security-in-github-codespaces)
- [Billing and included usage](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)
- [Create/resume links](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces)
- [ASUS specification](https://www.asus.com/displays-desktops/all-in-one-pcs/asus-aio/asus-m3402wfa/techspec/)
