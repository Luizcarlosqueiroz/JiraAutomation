from jira import JIRA
from datetime import datetime, timedelta
from getpass import getpass

def get_monday_week_date():
    today_datetime = datetime.now()

    monday_week_datetime = today_datetime - timedelta(days = today_datetime.weekday())

    monday_week_date = monday_week_datetime.date().strftime("%m-%d-%Y")

    return monday_week_date

password = getpass()

jira_connection = JIRA(
    basic_auth=('luiz.queiroz', password),
    server="https://issues.liferay.com/"
)

team_components = ['Workflow','Calendar','Forms','Data Engine']

team_test_suite = ['ci:test:workflow/workflow-metrics','ci:test:calendar','ci:test:forms','ci:test:data-engine']

monday_week_date = get_monday_week_date()

for component_name,test_suite in zip(team_components,team_test_suite):
    print(component_name,test_suite)

    issue_info = {
        "project": {"key": "LPS"},
        "summary": str(test_suite) + " - master - Week of " + str(monday_week_date),
        "description": "This ticket is for tracking analysis work done for the test suite in the summary field.\nTest Analysis Spreadsheet: https://docs.google.com/spreadsheets/d/13VUPfcOFRB__YFJNW20eV7o5zT4Lyz_3DuPSnuy2Q4E/edit#gid=1291581088",
        "issuetype": {"name": "Testing"},
        "components": [{"name": component_name}],
        "customfield_24523": {"value": "Analysis"},
    }

    new_issue = jira_connection.create_issue(fields=issue_info)

    print("https://issues.liferay.com/browse/" + str(new_issue))