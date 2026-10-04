# No Internet Connectivity

## Problem

Customer reports that Internet service is not working.

## Symptoms

Possible symptoms include:

- No Internet access
- Websites do not open
- Applications cannot connect
- Wi-Fi may be connected but Internet is unavailable

## Initial Checks

Check:

1. Customer account status
2. Payment/service status
3. ONU power status
4. ONU LOS status
5. Router power status
6. WAN/Internet status
7. Physical Ethernet connection
8. Wi-Fi connection status

## Customer-Side Checks

Ask the customer to:

1. Confirm the router is powered on.
2. Check the WAN/Internet indicator.
3. Check the ONU indicators.
4. Restart the ONU.
5. Wait for the ONU to stabilize.
6. Restart the router.
7. Test the connection again.

## NOC Diagnostics

If the issue persists, perform appropriate read-only
network diagnostics.

Possible diagnostics include:

- Ping
- DNS lookup
- TCP connectivity test
- Traceroute

## Possible Causes

Possible causes include:

- Customer router problem
- ONU problem
- Ethernet cable problem
- PPPoE authentication problem
- Upstream connectivity problem
- DNS problem
- Packet loss
- Routing problem
- Service/account issue

## Escalation

Escalate to the appropriate NOC/network team when:

- Customer-side checks are normal
- ONU status indicates a network-side issue
- Authentication continues to fail
- Significant packet loss is detected
- Upstream routing appears abnormal
- Multiple customers are affected
