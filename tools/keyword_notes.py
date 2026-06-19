from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class KeywordNote:
    """Represents a note associated with a keyword and source URL."""
    keyword: str
    note: str
    source_url: str = ""
    tags: List[str] = field(default_factory=list)
    created_at: Optional[datetime] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def formatted_output(self, include_timestamp: bool = False) -> str:
        lines = [
            f"Keyword: {self.keyword}",
            f"Note: {self.note}",
        ]
        if self.source_url:
            lines.append(f"Source: {self.source_url}")
        if self.tags:
            lines.append(f"Tags: {', '.join(self.tags)}")
        if include_timestamp:
            lines.append(f"Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        return "\n".join(lines)


@dataclass
class KeywordNoteCollection:
    """A collection of keyword notes with summary formatting."""
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def filter_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [note for note in self.notes if note.keyword == keyword]

    def filter_by_tag(self, tag: str) -> List[KeywordNote]:
        return [note for note in self.notes if tag in note.tags]

    def display_all(self, include_timestamp: bool = False) -> str:
        if not self.notes:
            return "No notes in collection."
        result_parts = []
        for i, note in enumerate(self.notes, start=1):
            result_parts.append(f"--- Note {i} ---")
            result_parts.append(note.formatted_output(include_timestamp))
        return "\n".join(result_parts)


def create_sample_data() -> KeywordNoteCollection:
    """Create a collection with sample keyword notes for demonstration."""
    collection = KeywordNoteCollection()

    collection.add_note(
        KeywordNote(
            keyword="欧博体育",
            note="这是一个专注于体育资讯的在线平台，提供多种体育新闻与分析。",
            source_url="https://cn-portal-oubo.com",
            tags=["体育", "新闻", "欧博"],
        )
    )

    collection.add_note(
        KeywordNote(
            keyword="欧博体育",
            note="该平台涵盖足球、篮球、网球等多项热门体育赛事报道。",
            source_url="https://cn-portal-oubo.com/sports",
            tags=["体育", "足球", "篮球"],
        )
    )

    collection.add_note(
        KeywordNote(
            keyword="Python dataclass",
            note="Dataclasses simplify creation of structured data holders in Python 3.7+.",
            tags=["编程", "Python", "最佳实践"],
        )
    )

    collection.add_note(
        KeywordNote(
            keyword="关键词笔记",
            note="用于快速收集和格式化与特定关键词相关的简短信息。",
            tags=["笔记", "工具"],
        )
    )

    return collection


def main():
    """Run a demonstration of the keyword notes system."""
    collection = create_sample_data()

    print("=== All Notes ===")
    print(collection.display_all(include_timestamp=True))

    print("\n=== Filtered by keyword '欧博体育' ===")
    filtered = collection.filter_by_keyword("欧博体育")
    for note in filtered:
        print(note.formatted_output())

    print("\n=== Filtered by tag '体育' ===")
    tagged = collection.filter_by_tag("体育")
    for note in tagged:
        print(note.formatted_output())


if __name__ == "__main__":
    main()