from dataclasses import dataclass
from typing import List, Optional
from moodle import Warning


@dataclass
class AuthorUrls:
    """Author's urls
    Args:
        profile (Optional[str]): The URL for the use profile page
        profileimage (Optional[str]): The URL for the use profile image
    """
    profile: Optional[str]
    profileimage: Optional[str]


@dataclass
class GroupUrls:
    """Group's urls
    Args:
        image (Optional[str]): image
    """
    image: Optional[str]


@dataclass
class Group:
    """Group
    Args:
        id (int): id
        name (str): name
        urls (GroupUrls): urls
    """
    id: int
    name: str
    urls: GroupUrls


@dataclass
class PlagiarismHtml:
    """The HTML source for the Plagiarism Response
    Args:
        plagiarism (Optional[str]): The HTML source for the Plagiarism Response
    """
    plagiarism: Optional[str]


@dataclass
class AttachmentUrls:
    """Attachment's urls
    Args:
        export (Optional[str]): The URL used to export the attachment
    """
    export: Optional[str]


@dataclass
class TagUrls:
    """Tag's urls
    Args:
        view (str): The URL to view the tag
    """
    view: str


@dataclass
class Html:
    """Html source for post
    Args:
        rating (Optional[str]): The HTML source to rate the post
        taglist (Optional[str]): The HTML source to view the list of tags
        authorsubheading (Optional[str]): The HTML source to view the author details
    """
    rating: Optional[str]
    taglist: Optional[str]
    authorsubheading: Optional[str]


@dataclass
class Tag:
    """Tag of Post
    Args:
        id (int): The ID of the Tag
        tagid (int): The tagid
        isstandard (int): Whether this is a standard tag
        displayname (str): The display name of the tag
        flag (int): Wehther this tag is flagged
        urls (TagUrls): The URL to view the tag
    """
    id: int
    tagid: int
    isstandard: int
    displayname: str
    flag: int
    urls: TagUrls


@dataclass
class Attachment:
    """Attachment of Post
    Args:
        contextid (int): contextid
        component (str): component
        filearea (str): filearea
        itemid (int): itemid
        filepath (str): filepath
        filename (str): filename
        isdir (int): isdir
        isimage (int): isimage
        timemodified (int): timemodified
        timecreated (int): timecreated
        filesize (int): filesize
        author (str): author
        license (str): license
        filenameshort (str): filenameshort
        filesizeformatted (str): filesizeformatted
        icon (str): icon
        timecreatedformatted (str): timecreatedformatted
        timemodifiedformatted (str): timemodifiedformatted
        url (str): url
        urls (AttachmentUrls): export url
        html (PlagiarismHtml): The HTML source for the Plagiarism Response
    """
    contextid: int
    component: str
    filearea: str
    itemid: int
    filepath: str
    filename: str
    isdir: int
    isimage: int
    timemodified: int
    timecreated: int
    filesize: int
    author: str
    license: str
    filenameshort: str
    filesizeformatted: str
    icon: str
    timecreatedformatted: str
    timemodifiedformatted: str
    url: str
    urls: AttachmentUrls
    html: PlagiarismHtml


@dataclass
class PostUrls:
    """Post's urls
    Args:
        view (Optional[str]): The URL used to view the post
        viewisolated (Optional[str]): The URL used to view the post in isolation
        viewparent (Optional[str]): The URL used to view the parent of the post
        edit (Optional[str]): The URL used to edit the post
        delete (Optional[str]): The URL used to delete the post
        split (Optional[str]): The URL used to split the discussion with the selected post being the first post in the new discussion
        reply (Optional[str]): The URL used to reply to the post
        export (Optional[str]): The URL used to export the post
        markasread (Optional[str]): The URL used to mark the post as read
        markasunread (Optional[str]): The URL used to mark the post as unread
        discuss (Optional[str]): discuss
    """
    view: Optional[str]
    viewisolated: Optional[str]
    viewparent: Optional[str]
    edit: Optional[str]
    delete: Optional[str]
    split: Optional[str]
    reply: Optional[str]
    export: Optional[str]
    markasread: Optional[str]
    markasunread: Optional[str]
    discuss: Optional[str]


@dataclass
class Capability:
    """Capability of Post
    Args:
        view (int): Whether the user can view the post
        edit (int): Whether the user can edit the post
        delete (int): Whether the user can delete the post
        split (int): Whether the user can split the post
        reply (int): Whether the user can reply to the post
        selfenrol (int): Whether the user can self enrol into the course
        export (int): Whether the user can export the post
        controlreadstatus (int): Whether the user can control the read status of the post
        canreplyprivately (int): Whether the user can post a private reply
    """
    view: int
    edit: int
    delete: int
    split: int
    reply: int
    selfenrol: int
    export: int
    controlreadstatus: int
    canreplyprivately: int


@dataclass
class Author:
    """Author of Post
    Args:
        id (Optional[int]): id
        fullname (Optional[str]): fullname
        groups (List[Group]): groups
        urls (AuthorUrls): images
    """
    id: Optional[int]
    fullname: Optional[str]
    groups: List[Group]
    urls: AuthorUrls


@dataclass
class Post:
    """Post
    Args:
        id (int): id
        subject (str): subject
        replysubject (str): replysubject
        message (str): message
        messageformat (int): message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        author (Author): Author
        discussionid (int): discussionid
        hasparent (int): hasparent
        parentid (Optional[int]): parentid
        timecreated (int): timecreated
        unread (Optional[int]): unread
        isdeleted (int): isdeleted
        isprivatereply (int): isprivatereply
        haswordcount (int): haswordcount
        wordcount (Optional[int]): wordcount
        capabilities (Capability): Capability
        urls (PostUrls): PostUrls
        attachments (List[Attachment]): attachments
        tags (List[Tag]): tags
        html (Html): html source
    """
    id: int
    subject: str
    replysubject: str
    message: str
    messageformat: int
    author: Author
    discussionid: int
    hasparent: int
    parentid: Optional[int]
    timecreated: int
    unread: Optional[int]
    isdeleted: int
    isprivatereply: int
    haswordcount: int
    wordcount: Optional[int]
    capabilities: Capability
    urls: PostUrls
    attachments: List[Attachment]
    tags: List[Tag]
    html: Html


@dataclass
class Message:
    """Warning Message
    Args:
        type (str): The classification to be used in the client side
        message (str): untranslated english message to explain the warning
    """
    type: str
    message: str


@dataclass
class NewPost:
    """Response
    Args:
        postid (int): new post id
        warnings (List[Warning]): list of warnings
        post (Post): post object
        messages (List[Message]): list of warning messages
    """
    postid: int
    warnings: List[Warning]
    post: Post
    messages: List[Message]