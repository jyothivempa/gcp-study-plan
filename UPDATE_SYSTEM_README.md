# Curriculum Update System

## Overview

This directory contains the **unified curriculum update system** that replaces the legacy weekly update scripts.

## Quick Start

```bash
# Update all curriculum content
python update_curriculum.py --all

# Update specific week
python update_curriculum.py --week 1

# Update specific day
python update_curriculum.py --day 5

# Preview changes (dry-run)
python update_curriculum.py --week 5 --dry-run
```

## Files

### Active System
- **`update_curriculum.py`** - Unified update script (replaces 7 legacy scripts)
- **`curriculum_config.yaml`** - Single source of truth for all 45 days of curriculum metadata

### Legacy Scripts (Archived)
- `legacy/update_week_1.py` through `legacy/update_week_7.py` - **Deprecated**
- These are kept for reference but should not be used

## Architecture Improvements

### Before (Legacy System)
❌ **7 separate scripts** with duplicate logic  
❌ **Hardcoded quiz data** in Python dictionaries  
❌ **Error-prone** - easy to make mistakes across different files  
❌ **Difficult to maintain** - changes required in multiple places

### After (New System)
✅ **Single unified script** - one source of truth  
✅ **YAML configuration** - easy to edit, no code required  
✅ **Quiz extraction from markdown** - content stays in markdown files  
✅ **Flexible filtering** - update by week, day, or all  
✅ **Dry-run mode** - preview changes before applying

## Configuration Format

The `curriculum_config.yaml` file defines all curriculum structure:

```yaml
days:
  - number: 1
    week: 1
    file: "section_1_cloud_fundamentals.md"
    title: "Cloud Fundamentals & The Google Difference"
    outcome: "Understand Cloud Computing Models"
```

## Quiz Extraction

Quizzes are automatically extracted from markdown files using this format:

```markdown
<!-- Quizzes can be in HTML comments -->
**Q1. What is Google Cloud Platform?**
A. A hardware vendor
B. A cloud computing platform
C. An operating system
D. A database

> **Answer: B.** GCP is Google's cloud platform.
```

## Migration Guide

If you were using the old scripts:

```bash
# OLD (deprecated)
python update_week_1.py
python update_week_2.py
# ... etc

# NEW (unified)
python update_curriculum.py --all
```

## Adding New Days

1. **Edit `curriculum_config.yaml`** - Add new day entry
2. **Create markdown file** - Add content file in `curriculum/content/`
3. **Run update** - `python update_curriculum.py --day X`

No code changes required!

## Troubleshooting

### No quizzes found
- Verify quiz format in markdown matches pattern: `**Q1. question text?**`
- Check that Answer line uses format: `> **Answer: B.**`
- Quizzes can be in regular content or HTML comments

### File not found
- Verify `file` path in `curriculum_config.yaml` matches actual filename
- Files should be in `curriculum/content/` directory

### Database not updating
- Remove `--dry-run` flag
- Verify Django is configured properly
- Check console output for specific error messages

## Benefits

1. **Single Source of Truth** - All curriculum structure in one YAML file
2. **Easy Maintenance** - Add/modify days without touching Python code
3. **Less Error-Prone** - No duplicate logic across multiple files
4. **Better Automation** - Can update entire curriculum with one command
5. **Version Controlled** - YAML changes are easy to review in Git

## Future Enhancements

- [ ] Validate YAML schema on load
- [ ] Auto-detect content files
- [ ] Support for different question types beyond MCQ
- [ ] Integration with CI/CD pipeline
- [ ] Rollback capability for quiz changes
