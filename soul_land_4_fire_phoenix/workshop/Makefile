.PHONY: validate validate-current validate-recovery validate-github backup

# Run governance, recovery, historical, V2, staging, and accepted-snapshot checks.
validate:
	python3 tools/validate_all.py

# Run only the active protected V2 and locally accepted snapshot checks.
validate-current:
	python3 tools/validate_current_v2_line.py
	python3 tools/validate_local_accepted_v2_release.py

# Run only recovered public-evidence checks.
validate-recovery:
	python3 tools/verify_public_recovery.py
	python3 tools/validate_workshop.py

# Check GitHub workflow hardening, governance assets, and tracked-content credential screen.
validate-github:
	python3 tools/validate_github_governance.py

# Create a verified local-only Git bundle in ignored backups/.
backup:
	bash tools/create_git_bundle_backup.sh
