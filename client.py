class WorkflowAgentScaffolderOpsClient:
    def create_scaffold(self, template_name: str) -> dict:
        return {"scaffold_path": "/templates/default_agent.py"}