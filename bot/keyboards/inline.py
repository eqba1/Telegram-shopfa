from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.locales import translate


def main_menu(role: int, channel: str = None, helper: str = None) -> InlineKeyboardMarkup:
    inline_keyboard = [
        [
            InlineKeyboardButton(translate('shop'), callback_data='shop'),
            InlineKeyboardButton(translate('rules'), callback_data='rules'),
        ],
        [InlineKeyboardButton(translate('profile'), callback_data='profile')],
    ]
    if helper and channel:
        inline_keyboard.append([
            InlineKeyboardButton(translate('support'), url=f"https://t.me/{helper.lstrip('@')}"),
            InlineKeyboardButton(translate('news_channel'), url=f"https://t.me/{channel}")
        ])
    else:
        if helper:
            inline_keyboard.append([InlineKeyboardButton(translate('support'), url=f"https://t.me/{helper.lstrip('@')}")])
        if channel:
            inline_keyboard.append(
                [InlineKeyboardButton(translate('news_channel'), url=f"https://t.me/{channel}")])
    if role > 1:
        inline_keyboard.append([InlineKeyboardButton(translate('admin_panel'), callback_data='console')])

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def categories_list(list_items: list[str], current_index: int, max_index: int) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    page_items = list_items[current_index * 10: (current_index + 1) * 10]
    for name in page_items:
        markup.add(InlineKeyboardButton(text=name, callback_data=f'category_{name}'))
    if max_index > 0:
        buttons = [
            InlineKeyboardButton(text='◀️', callback_data=f'categories-page_{current_index - 1}'),
            InlineKeyboardButton(text=f'{current_index + 1}/{max_index + 1}', callback_data='dummy_button'),
            InlineKeyboardButton(text='▶️', callback_data=f'categories-page_{current_index + 1}')
        ]
        markup.row(*buttons)
    markup.add(InlineKeyboardButton(translate('back_to_menu'), callback_data='back_to_menu'))
    return markup


def goods_list(list_items: list[str], category_name: str, current_index: int, max_index: int) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    page_items = list_items[current_index * 10: (current_index + 1) * 10]
    for name in page_items:
        markup.add(InlineKeyboardButton(text=name, callback_data=f'item_{name}'))
    if max_index > 0:
        buttons = [
            InlineKeyboardButton(text='◀️', callback_data=f'goods-page_{category_name}_{current_index - 1}'),
            InlineKeyboardButton(text=f'{current_index + 1}/{max_index + 1}', callback_data='dummy_button'),
            InlineKeyboardButton(text='▶️', callback_data=f'goods-page_{category_name}_{current_index + 1}')
        ]
        markup.row(*buttons)
    markup.add(InlineKeyboardButton(translate('back'), callback_data='shop'))
    return markup


def user_items_list(list_items: list, data: str, back_data: str, pre_back: str, current_index: int, max_index: int)\
        -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    page_items = list_items[current_index * 10: (current_index + 1) * 10]
    for item in page_items:
        markup.add(InlineKeyboardButton(text=item.item_name, callback_data=f'bought-item:{item.id}:{pre_back}'))
    if max_index > 0:
        buttons = [
            InlineKeyboardButton(text='◀️', callback_data=f'bought-goods-page_{current_index - 1}_{data}'),
            InlineKeyboardButton(text=f'{current_index + 1}/{max_index + 1}', callback_data='dummy_button'),
            InlineKeyboardButton(text='▶️', callback_data=f'bought-goods-page_{current_index + 1}_{data}')
        ]
        markup.row(*buttons)
    markup.add(InlineKeyboardButton(translate('back'), callback_data=back_data))
    return markup


def item_info(item_name: str, category_name: str) -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('buy'), callback_data=f'buy_{item_name}')],
        [InlineKeyboardButton(translate('back'), callback_data=f'category_{category_name}')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def profile(referral_percent: int, user_items: int = 0) -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('replenish_balance'), callback_data='replenish_balance')
         ]
    ]
    if referral_percent != 0:
        inline_keyboard.append([InlineKeyboardButton(translate('referral_system'), callback_data='referral_system')])
    if user_items != 0:
        inline_keyboard.append([InlineKeyboardButton(translate('bought_items'), callback_data='bought_items')])
    inline_keyboard.append([InlineKeyboardButton(translate('back_to_menu'), callback_data='back_to_menu')])
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def rules() -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('back_to_menu'), callback_data='back_to_menu')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def console() -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('manage_goods'), callback_data='shop_management')
         ],
        [InlineKeyboardButton(translate('manage_users'), callback_data='user_management')
         ],
        [InlineKeyboardButton(translate('broadcast'), callback_data='send_message')
         ],
        [InlineKeyboardButton(translate('back_to_menu'), callback_data='back_to_menu')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def user_management(admin_role: int, user_role: int, admin_manage: int, items: int, user_id: int) \
        -> InlineKeyboardMarkup:
    inline_keyboard = [
        [
            InlineKeyboardButton(translate('fill_user_balance'), callback_data=f'fill-user-balance_{user_id}')
        ]
    ]
    if items > 0:
        inline_keyboard.append([InlineKeyboardButton(translate('bought_items'), callback_data=f'user-items_{user_id}')])
    if admin_role >= admin_manage and admin_role > user_role:
        if user_role == 1:
            inline_keyboard.append(
                [InlineKeyboardButton(translate('appoint_admin'), callback_data=f'set-admin_{user_id}')])
        else:
            inline_keyboard.append(
                [InlineKeyboardButton(translate('remove_admin'), callback_data=f'remove-admin_{user_id}')])
    inline_keyboard.append([InlineKeyboardButton(translate('back'), callback_data='user_management')])
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def user_manage_check(user_id: int) -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('yes'), callback_data=f'check-user_{user_id}')
         ],
        [InlineKeyboardButton(translate('back'), callback_data='user_management')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def shop_management() -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('manage_goods'), callback_data='goods_management')
         ],
        [InlineKeyboardButton(translate('manage_categories'), callback_data='categories_management')
         ],
        [InlineKeyboardButton(translate('show_logs'), callback_data='show_logs')
         ],
        [InlineKeyboardButton(translate('statistics'), callback_data='statistics')
         ],
        [InlineKeyboardButton(translate('back'), callback_data='console')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def goods_management() -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('add_item'), callback_data='item-management'),
         InlineKeyboardButton(translate('update_item'), callback_data='update_item'),
         InlineKeyboardButton(translate('delete_item'), callback_data='delete_item')
         ],
        [InlineKeyboardButton(translate('show_bought_item'), callback_data='show_bought_item')
         ],
        [InlineKeyboardButton(translate('back'), callback_data='shop_management')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def item_management() -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('create_item'), callback_data='add_item'),
         InlineKeyboardButton(translate('add_item_existing'), callback_data='update_item_amount'),
         ],
        [InlineKeyboardButton(translate('back'), callback_data='goods_management')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def categories_management() -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('add_category'), callback_data='add_category'),
         InlineKeyboardButton(translate('update_category'), callback_data='update_category'),
         InlineKeyboardButton(translate('delete_category'), callback_data='delete_category')
         ],
        [InlineKeyboardButton(translate('back'), callback_data='shop_management')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def close() -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('hide'), callback_data='close')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def check_sub(channel_username: str) -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('subscribe'), url=f'https://t.me/{channel_username}')
         ],
        [InlineKeyboardButton(translate('check'), callback_data='sub_channel_done')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def back(callback: str) -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('back'), callback_data=callback)
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def payment_menu(url: str, label: str) -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('pay'), url=url)
         ],
        [InlineKeyboardButton(translate('check_pay'), callback_data=f'check_{label}')
         ],
        [InlineKeyboardButton(translate('back'), callback_data='replenish_balance')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def reset_config(key: str) -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(f'Сбросить {key}', callback_data=f'reset_{key}')
         ],
        [InlineKeyboardButton('🔙 Вернуться назад', callback_data='settings')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def question_buttons(question: str, back_data: str) -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(translate('yes'), callback_data=f'{question}_yes'),
         InlineKeyboardButton(translate('no'), callback_data=f'{question}_no')
         ],
        [InlineKeyboardButton(translate('back'), callback_data=back_data)
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
