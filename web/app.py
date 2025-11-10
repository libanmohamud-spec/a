#!/usr/bin/env python3
"""
Simple web dashboard for participants to view their progress.

Run with: python web/app.py
Access at: http://localhost:4311
"""
import json
from pathlib import Path
from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder='templates')

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"


def load_assignment(pid: str) -> dict:
    """Load assignment.json for a participant."""
    assignment_path = RESULTS_DIR / pid / "assignment.json"
    if not assignment_path.exists():
        return None
    return json.loads(assignment_path.read_text(encoding="utf-8"))


def load_round_results(pid: str, round_num: str) -> dict:
    """Load results.json for a round."""
    results_path = RESULTS_DIR / pid / f"round{round_num}" / "results.json"
    if not results_path.exists():
        return None
    return json.loads(results_path.read_text(encoding="utf-8"))


def load_round_meta(pid: str, round_num: str) -> dict:
    """Load meta.json for a round."""
    meta_path = RESULTS_DIR / pid / f"round{round_num}" / "meta.json"
    if not meta_path.exists():
        return None
    return json.loads(meta_path.read_text(encoding="utf-8"))


@app.route('/')
def index():
    """Main dashboard page."""
    return render_template('index.html')


@app.route('/api/participant/<participant_id>')
def get_participant_data(participant_id):
    """Get participant data as JSON."""
    assignment = load_assignment(participant_id)
    if not assignment:
        return jsonify({"error": "Participant not found"}), 404
    
    data = {
        "participant_id": participant_id,
        "experienced": assignment.get("experienced", False),
        "assignments": assignment.get("assignments", {}),
        "allow_llm": assignment.get("allow_llm", {}),
        "rounds": {}
    }
    
    for round_num in ["1", "2"]:
        results = load_round_results(participant_id, round_num)
        meta = load_round_meta(participant_id, round_num)
        
        round_data = {
            "submitted": meta is not None,
            "submitted_at": meta.get("submitted_at") if meta else None,
            "exit_code": meta.get("exit_code") if meta else None,
        }
        
        if results:
            summary = results.get("summary", {})
            round_data["tests"] = {
                "total": summary.get("total", 0),
                "passed": summary.get("passed", 0),
                "failed": summary.get("failed", 0),
                "errors": summary.get("error", 0),
            }
        else:
            round_data["tests"] = None
        
        data["rounds"][f"round{round_num}"] = round_data
    
    return jsonify(data)


@app.route('/api/participants')
def list_participants():
    """List all participants."""
    participants = []
    if RESULTS_DIR.exists():
        for pid_dir in RESULTS_DIR.iterdir():
            if pid_dir.is_dir() and (pid_dir / "assignment.json").exists():
                assignment = load_assignment(pid_dir.name)
                if assignment:
                    participants.append({
                        "id": pid_dir.name,
                        "experienced": assignment.get("experienced", False),
                    })
    return jsonify({"participants": sorted(participants, key=lambda x: x["id"])})


if __name__ == '__main__':
    # Run on port 4311 (Codespaces will forward this)
    app.run(host='0.0.0.0', port=4311, debug=True)

