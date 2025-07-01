from aqt import mw
from aqt.gui_hooks import profile_did_open
from anki.models import ModelManager, NotetypeDict

def setup_interactive_mcq_note_type():
    mm = mw.col.models
    model_name = "Interactive MCQ"
    
    # Check if model exists
    model = mm.by_name(model_name)
    if model:
        return
    
    # Create new model
    model = mm.new(model_name)
    
    # Add fields
    fields = [
        {"name": "Question_Statement"},
        {"name": "Option_1"},
        {"name": "Option_2"},
        {"name": "Option_3"},
        {"name": "Option_4"},
        {"name": "Option_5"},
        {"name": "Correct_Answer"},
        {"name": "Explanation"}
    ]
    for field in fields:
        fm = mm.new_field(field["name"])
        mm.add_field(model, fm)
    
    # Add templates
    template = mm.new_template("Card 1")
    
    # Front Template
    template['qfmt'] = """
    <div class="mcq-card">
      <!-- PASTE FRONT TEMPLATE HTML HERE -->
    </div>
    <script>
      <!-- PASTE JAVASCRIPT CODE HERE -->
    </script>
    """
    
    # Back Template
    template['afmt'] = """
    {{FrontSide}}
    <hr class="divider">
    <!-- PASTE BACK TEMPLATE HTML HERE -->
    """
    
    # CSS Styling
    model['css'] = """
    /* PASTE CSS STYLING HERE */
    """
    
    mm.add_template(model, template)
    mm.add(model)
    mm.save(model)

# Register setup function
profile_did_open.append(setup_interactive_mcq_note_type)
