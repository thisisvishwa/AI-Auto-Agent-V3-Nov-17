```python
import json
from typing import Dict

class PrivacyLawsCompliance:
    def __init__(self, user_data: Dict):
        self.user_data = user_data

    def check_gdpr_compliance(self):
        """
        Check if the user data complies with GDPR.
        """
        if self.user_data.get('eu_resident'):
            if not self.user_data.get('consent'):
                raise ValueError("EU residents must give consent for data processing.")
        return True

    def check_ccpa_compliance(self):
        """
        Check if the user data complies with CCPA.
        """
        if self.user_data.get('california_resident'):
            if not self.user_data.get('consent'):
                raise ValueError("California residents must give consent for data processing.")
        return True

    def check_pipeda_compliance(self):
        """
        Check if the user data complies with PIPEDA.
        """
        if self.user_data.get('canada_resident'):
            if not self.user_data.get('consent'):
                raise ValueError("Canadian residents must give consent for data processing.")
        return True

    def check_compliance(self):
        """
        Check if the user data complies with all privacy laws.
        """
        self.check_gdpr_compliance()
        self.check_ccpa_compliance()
        self.check_pipeda_compliance()
        return True

if __name__ == "__main__":
    # Load user data from a JSON file
    with open('user_data.json', 'r') as f:
        user_data = json.load(f)

    # Create a PrivacyLawsCompliance object
    compliance_checker = PrivacyLawsCompliance(user_data)

    # Check compliance
    if compliance_checker.check_compliance():
        print("User data is compliant with all privacy laws.")
```
