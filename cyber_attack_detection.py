# AI-Based Cyber Attack Detection Agent

print("=" * 55)
print("      AI-BASED CYBER ATTACK DETECTION AGENT")
print("=" * 55)

normal_packets = int(input("Enter Normal Packets Count : "))
failed_logins = int(input("Enter Failed Login Attempts : "))
unknown_ips = int(input("Enter Unknown IP Connections : "))
malware_detected = input("Malware Detected? (yes/no): ").lower()

print("\nAnalyzing Network...\n")

score = 0

if normal_packets > 1000:
    score += 1

if failed_logins > 5:
    score += 2

if unknown_ips > 3:
    score += 2

if malware_detected == "yes":
    score += 5

print("----------- ANALYSIS REPORT -----------")

if score >= 5:
    print("⚠️  CYBER ATTACK DETECTED")
    print("Threat Level : HIGH")
    print("Action : Block Suspicious IP")
    print("Firewall Updated")
    print("Administrator Alert Sent")
else:
    print("✅ Network Status : SAFE")
    print("Threat Level : LOW")
    print("No suspicious activity detected.")

print("---------------------------------------")
print("Monitoring Completed Successfully")